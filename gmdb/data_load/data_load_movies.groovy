// load movies
new File(path + '/movies.dat').eachLine { def line ->
    def components = line.split('::');
    def movieVertex = g.addVertex(['element_type':'movie', 'movie_id':components[0].toInteger(), 'movie_title': components[1]]);
    components[2].split('\\|').each { def genre ->
        def hits = g.V.has('genre_genre', genre);
        def genreVertex = hits.hasNext() ? hits.next() : g.addVertex(['element_type':'genre', 'genre_genre': genre]);
        g.addEdge(movieVertex, genreVertex, 'has_genre');
    }
}

g.commit()
