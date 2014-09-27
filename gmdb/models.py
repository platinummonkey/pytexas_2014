from mogwai.models import Vertex, Edge
from mogwai.models.vertex import EnumVertexBaseMeta
from mogwai import properties
from mogwai import relationships
from mogwai import gremlin
import os

cwd = os.path.dirname(os.path.realpath(__file__))
groovy_path = os.path.join(cwd, 'models.groovy')


class HasOccupation(Edge):
    """ Identifying user occupation(s) """

    label = 'has_occupation'


class Occupation(Vertex):
    """ A User's Occupation """

    __metaclass__ = EnumVertexBaseMeta
    __enum_id_only__ = False
    element_type = 'occupation'

    occupation = properties.String(required=True)

    count = gremlin.GremlinValue(path=groovy_path, method_name='obj_count', classmethod=True,
                                 defaults={'element_type': 'occupation'})
    get_distribution = gremlin.GremlinMethod(path=groovy_path, method_name='occupation_distribution',
                                             classmethod=True, defaults={'element_type': 'user'})

    def enum_generator(self):
        return self.occupation.replace('/', '_').replace(' ', '_').replace('-', '_').upper()


class HasGenre(Edge):
    """ Identify which Genre(s) a Movie has """

    label = 'has_genre'


class Genre(Vertex):
    """ A specifc Genre

    Movies can have multiple genres
    """

    element_type = 'genre'

    genre = properties.String(required=True)

    count = gremlin.GremlinValue(path=groovy_path, method_name='obj_count', classmethod=True,
                                 defaults={'element_type': 'genre'})


class Rated(Edge):
    """ A User rating for a Movie """

    label = 'rated'

    stars = properties.PositiveInteger(required=True, default=0, choices=[0, 1, 2, 3, 4, 5])


class Movie(Vertex):
    """ A Movie """

    element_type = 'movie'

    title = properties.String(required=True)

    count = gremlin.GremlinValue(path=groovy_path, method_name='obj_count', classmethod=True,
                                 defaults={'element_type': 'movie'})

    get_users_given_movie_with_rating_above = gremlin.GremlinMethod(path=groovy_path,
                                                                    method_name='users_given_movie_with_rating_above',
                                                                    defaults={'limit': 4, 'stars': 3})

    get_movies_with_user_ratings_above = gremlin.GremlinMethod(path=groovy_path,
                                                               method_name='movies_with_user_ratings_above',
                                                               defaults={'stars': 3, 'limit': 4})

    get_corated_movie = gremlin.GremlinMethod(path=groovy_path, method_name='corated_movie_from_movie',
                                              defaults={'stars': 3, 'limit': 9})

    get_corated_movie_by_genre = gremlin.GremlinMethod(path=groovy_path, method_name='corated_movie_by_genre',
                                                       defaults={'stars': 3, 'limit': 9})

    get_corated_movie_by_all_genres = gremlin.GremlinMethod(path=groovy_path,
                                                            method_name='corated_movie_by_genre_has_all',
                                                            defaults={'stars': 3, 'limit': 9})


class User(Vertex):
    """ A User """

    element_type = 'user'

    gender = properties.String(required=True, choices=['M', 'F'])
    age = properties.PositiveInteger(required=True, default=0)

    count = gremlin.GremlinValue(path=groovy_path, method_name='obj_count', classmethod=True,
                                 defaults={'element_type': 'user'})

    get_mean_age = gremlin.GremlinValue(path=groovy_path, method_name='user_mean_age', classmethod=True,
                                        defaults={'element_type': 'user'})