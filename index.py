from bottle import Bottle, run, request, response, abort, redirect, jinja2_view as view, static_file
from bottle_memcache import MemcachePlugin
from mogwai.connection import setup, execute_query
from models import *
from tools import groupCountToObjValueMap

setup('localhost', concurrency='eventlet')

app = Bottle()
mc_plugin = MemcachePlugin(servers=['localhost:11211', ])
app.install(mc_plugin)


@app.error(404)
def error404(error):
    return "Nothing here."


@app.route('/static/<path:path>')
def callback(path):
    path = path.replace('../', '').strip(';')
    return static_file(path, 'views/static/')


@app.get('/', apply=[view('index')])
def index(mc):
    counts = mc.get('index_counts')
    if not counts:
        user_count = User.count()
        occupation_count = Occupation.count()
        movie_count = Movie.count()
        vertex_count = execute_query('g.V.count()')
        edge_count = execute_query('g.E.count()')
        counts = {'movieCount': movie_count,
                  'occupationCount': occupation_count,
                  'userCount': user_count,
                  'vertexCount': vertex_count,
                  'edgeCount': edge_count}
        mc.set('index_counts', counts)
        return counts
    return counts


@app.get('/about', apply=[view('about')])
def about():
    return {}

@app.get('/user/occupations', apply=[view('user/occupation_distribution')])
def get_user_occupation_distribution(mc):
    distribution = mc.get('user_occupationDistribution')
    if not distribution:
        distribution = groupCountToObjValueMap(Occupation.get_distribution())
        mc.set('user_occupationDistribution', distribution)
    code = '''def occupation_distribution(element_type) {
    def m = [:]
    g.V.has('element_type', element_type)                // Filter Users first
       .out('has_occupation')                            // Find Occupation Edges
       .groupCount(m).iterate()                          // Group unique vertices and count
    return m.sort{a, b -> b.value <=> a.value}[0..4]     // Sort by group count and return top N
}'''
    return {'distribution': distribution, 'code': code}


@app.get('/user/meanAge', apply=[view('user/mean_age')])
def get_user_mean_age(mc):
    mean_age = mc.get('user_meanAge')
    if not mean_age:
        mean_age = User.get_mean_age()
        mc.set('user_meanAge', mean_age)
    code = '''def user_mean_age(element_type) {
    return g.V('element_type', element_type)  // Filter by Users
            .user_age                         // We only care about their age
            .mean()                           // Find the mean over all the User vertices
}'''
    return {'mean_age': mean_age, 'code': code}


@app.get('/movie/all', apply=[view('movie/movies')])
def all_movies(mc):
    movies = mc.get('movie_all')
    if not movies:
        movies = Movie.all()
        mc.set('movie_all', movies)
    return {'movies': movies}


@app.get('/movie/<movie_id:int>', apply=[view('movie/info')])
def get_movie(movie_id, mc):
    movie = mc.get('movie_{}'.format(movie_id))
    if not movie:
        movie = Movie.get(movie_id)
        mc.set('movie_{}'.format(movie_id), movie)
    return {'movie': movie, 'code': 'ids.collect{g.v(it)} // where `ids` is a parameter defines as a list of ints'}


@app.get('/movie/<movie_id:int>/usersWithRatingsAbove', apply=[view('movie/users_with_ratings_above')])
def users_given_movie_with_rating_above(movie_id, mc):
    stars = int(request.query.stars or 3)
    limit = int(request.query.limit or 5)
    cache = mc.get('users_with_ratings_above_{}_{}_{}'.format(movie_id, stars, limit))
    code = '''def users_given_movie_with_rating_above(id, stars, limit) {
    def v = g.v(id)                                      // Get the Movie
    return v.inE('rated')                                // Using a vertex centric query, find ratings
            .filter{ it.getProperty('stars') > stars }   // Filter to find ratings above criterion
            .outV[0..limit-1]                              // Return Users and return first N
}'''
    if not cache:
        movie = Movie.get(movie_id)
        users = movie.get_users_given_movie_with_rating_above(stars=stars, limit=limit)
        mc.set('users_with_ratings_above_{}_{}_{}'.format(movie_id, stars, limit),
               {'movie': movie, 'users': users, 'stars': stars, 'limit': limit})
        return {'movie': movie, 'users': users, 'stars': stars, 'code': code, 'limit': limit}
    else:
        cache['code'] = code
    return cache


@app.get('/movie/<movie_id:int>/moviesWithRatingsAbove', apply=[view('movie/movies_with_ratings_above')])
def movies_given_movie_with_rating_above(movie_id, mc):
    stars = int(request.query.stars or 3)
    limit = int(request.query.limit or 5)
    cache = mc.get('movies_with_ratings_above_{}_{}_{}'.format(movie_id, stars, limit))
    code = '''def movies_with_user_ratings_above(id, stars, limit) {
    def v = g.v(id)                                      // Get the Movie
    return v.inE('rated')                                // Using a vertex centric query, find ratings
            .filter{ it.getProperty('stars') > stars }   // Filter to find ratings above criterion
            .outV.outE('rated')                          // Find other movie's ratings
            .filter{ it.getProperty('stars') > stars }   // Repeat filter to find ratings above criterion
            .inV                                         // Get the Movie associated
            .dedup[0..limit-1]                             // Deduplicate the Movie results and return top N
}'''
    if not cache:
        movie = Movie.get(movie_id)
        movies = movie.get_movies_with_user_ratings_above(stars=stars, limit=limit)
        mc.set('movies_with_ratings_above_{}_{}_{}'.format(movie_id, stars, limit),
               {'movie': movie, 'movies': movies, 'stars': stars})
        return {'movie': movie, 'movies': movies, 'stars': stars, 'code': code}
    else:
        cache['code'] = code
    return cache


@app.get('/movie/<movie_id:int>/coratedMovie', apply=[view('movie/corated_movie_from_movie')])
def corated_movie_from_movie(movie_id, mc):
    stars = int(request.query.stars or 3)
    limit = int(request.query.limit or 5)
    cache = mc.get('corated_movie_from_movie_{}_{}_{}'.format(movie_id, stars, limit))
    code = '''def corated_movie_from_movie(id, stars, limit) {
    def v = g.v(id)                                                // Get the Movie
    def m = [:]                                                    // Initialize Empty HashMap
    def r = [:]
    v.inE('rated')                                                 // Using a vertex centric query, find ratings
      .filter{ it.getProperty('stars') > stars }                   // Filter to find ratings above criterion
      .outV.outE('rated')                                          // Find other movie's ratings
      .filter{ it.getProperty('stars') > stars }                   // Repeat filter to find ratings above criterion
      .inV                                                         // Get the Movie associated
      .filter{ it != v }                                           // Don't allow the original Movie to show up
      .groupCount(m).iterate()                                     // Group by unique Movie and count
    return m.sort{a, b -> b.value <=> a.value}.take(limit.toInteger())   // Sort by group count and return top N
}'''
    if not cache:
        movie = Movie.get(movie_id)
        movies = groupCountToObjValueMap(movie.get_corated_movie(stars=stars, limit=limit))
        mc.set('corated_movie_from_movie_{}_{}_{}'.format(movie_id, stars, limit),
               {'movie': movie, 'movies': movies, 'stars': stars})
        return {'movie': movie, 'movies': movies, 'stars': stars, 'code': code}
    else:
        cache['code'] = code
    return cache


@app.get('/movie/<movie_id:int>/coratedMovieByGenre', apply=[view('movie/corated_movie_by_genre')])
def corated_movie_by_genre(movie_id, mc):
    stars = int(request.query.stars or 3)
    limit = int(request.query.limit or 5)
    cache = mc.get('corated_movie_by_genre_{}_{}_{}'.format(movie_id, stars, limit))
    code = '''def corated_movie_by_genre(id, stars, limit) {
    def v = g.v(id)                                       // Get the Movie
    def m = [:]                                           // Initialize Empty HashMap
    def x = [] as Set                                     // Initialize empty Set
    v.out('has_genre')                                    // Using a vertex centric query, find genres
     .aggregate(x)                                        // Add genres to Set for reference
     .back(2)                                             // Go back 2 steps to the original Movie
     .inE('rated')                                        // Using a vertex centric query, find ratings
     .filter{ it.getProperty('stars') > stars }           // Filter to find ratings above criterion
     .outV.outE('rated')                                  // Find other movie's ratings
     .filter{ it.getProperty('stars') > stars }           // Repeat filter to find ratings above criterion
     .inV                                                 // Get the Movie associated
     .filter{ it != v }                                   // Don't allow the original Movie to show up
     .out('has_genre')                                    // Find Genres associated
     .retain(x)                                           // Only allow what was in the stored Set to pass validation (filter out movies without the genre in question)
     .back(2)                                             // Go Back 2 steps
     .groupCount(m).iterate()                             // Group by unique Movie and count
    return m.sort{a, b -> b.value <=> a.value}.take(limit.toInteger())   // Sort by group count and return top N
}'''
    if not cache:
        movie = Movie.get(movie_id)
        movies = groupCountToObjValueMap(movie.get_corated_movie_by_genre(stars=stars, limit=limit))
        mc.set('corated_movie_by_genre_{}_{}_{}'.format(movie_id, stars, limit),
               {'movie': movie, 'movies': movies, 'stars': stars})
        return {'movie': movie, 'movies': movies, 'stars': stars, 'code': code}
    else:
        cache['code'] = code
    return cache


@app.get('/movie/<movie_id:int>/coratedMovieByAllGenre', apply=[view('movie/corated_movie_by_all_genre')])
def corated_movie_by_genre(movie_id, mc):
    stars = int(request.query.stars or 3)
    limit = int(request.query.limit or 5)
    cache = mc.get('corated_movie_by_genre_all_{}_{}_{}'.format(movie_id, stars, limit))
    code = '''def corated_movie_by_genre_has_all(id, stars, limit) {
    def v = g.v(id)
    def m = [:]
    def x = [] as Set
    v.out('has_genre')
     .aggregate(x)
     .back(2)
     .inE('rated')
     .filter{ it.getProperty('stars') > stars }
     .outV.outE('rated')
     .filter{ it.getProperty('stars') > stars}
     .inV
     .filter{ it != v}
     .filter{ it.out('has_genre').toList() as Set == x}
     .groupCount(m).iterate()
    return m.sort{a, b -> b.value <=> a.value}.take(limit.toInteger())   // Sort by group count and return top N
}'''
    if not cache:
        movie = Movie.get(movie_id)
        movies = groupCountToObjValueMap(movie.get_corated_movie_by_all_genres(stars=stars, limit=limit))
        mc.set('corated_movie_by_genre_all_{}_{}_{}'.format(movie_id, stars, limit),
               {'movie': movie, 'movies': movies, 'stars': stars})
        return {'movie': movie, 'movies': movies, 'stars': stars, 'code': code}
    else:
        cache['code'] = code
    return cache


if __name__ == '__main__':
    app.run(host='localhost', port=8080, debug=True)