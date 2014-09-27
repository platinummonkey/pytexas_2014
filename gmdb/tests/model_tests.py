from tests.base import BaseTestCase
from models import *


class ModelTests(BaseTestCase):

    def testOccupationDistribution(self):
        d = Occupation.get_distribution()
        self.assertEqual(len(d), 5)
        self.assertListEqual([o['_value'] for o in d.values()], [759, 711, 502, 528, 679])

    def testUserMeanAge(self):
        ma = User.get_mean_age()
        self.assertAlmostEqual(ma, 30.639238410596025, places=15)

    def testObjectCount(self):
        self.assertEqual(Occupation.count(), 21)

    def get_toy_story_movie(self):
        return Movie.find_by_value('movie_title', 'Toy Story (1995)')[0]

    def testUsersGivenMovieWithRatingAbove(self):
        m = self.get_toy_story_movie()
        r = m.get_users_given_movie_with_rating_above(limit=5)
        self.assertEqual(len(r), 5)

    def testMoviesWithUserRatingsAbove(self):
        m = self.get_toy_story_movie()
        r = m.get_movies_with_user_ratings_above(limit=5)
        self.assertEqual(len(r), 5)

    def testCoratedMovies(self):
        m = self.get_toy_story_movie()
        r = m.get_corated_movie(limit=5)
        self.assertEqual(len(r), 5)
        self.assertEqual(r.values()[0]['_value'], 1000)
        self.assertEqual(r.values()[0]['_key'].title, 'Star Wars: Episode V - The Empire Strikes Back (1980)')
        self.assertEqual(r.values()[1]['_value'], 998)
        self.assertEqual(r.values()[1]['_key'].title, 'Star Wars: Episode IV - A New Hope (1977)')
        self.assertEqual(r.values()[2]['_value'], 922)
        self.assertEqual(r.values()[2]['_key'].title, 'Raiders of the Lost Ark (1981)')
        self.assertEqual(r.values()[3]['_value'], 949)
        self.assertEqual(r.values()[3]['_key'].title, 'American Beauty (1999)')
        self.assertEqual(r.values()[4]['_value'], 925)
        self.assertEqual(r.values()[4]['_key'].title, 'Matrix, The (1999)')

    def testCoratedMovieByGenre(self):
        m = self.get_toy_story_movie()
        r = m.get_corated_movie_by_genre(limit=5)
        self.assertEqual(len(r), 5)
        self.assertEqual(r.values()[0]['_value'], 949)
        self.assertEqual(r.values()[0]['_key'].title, 'American Beauty (1999)')
        self.assertEqual(r.values()[1]['_value'], 876)
        self.assertEqual(r.values()[1]['_key'].title, 'Back to the Future (1985)')
        self.assertEqual(r.values()[2]['_value'], 851)
        self.assertEqual(r.values()[2]['_key'].title, 'Princess Bride, The (1987)')
        self.assertEqual(r.values()[3]['_value'], 871)
        self.assertEqual(r.values()[3]['_key'].title, 'Toy Story 2 (1999)')
        self.assertEqual(r.values()[4]['_value'], 843)
        self.assertEqual(r.values()[4]['_key'].title, 'Groundhog Day (1993)')

    def testCoratedMovieByGenreInclusive(self):
        m = self.get_toy_story_movie()
        r = m.get_corated_movie_by_all_genres(limit=5)
        self.assertEqual(len(r), 5)
        self.assertEqual(r.values()[0]['_value'], 871)
        self.assertEqual(r.values()[0]['_key'].title, 'Toy Story 2 (1999)')
        self.assertEqual(r.values()[1]['_value'], 700)
        self.assertEqual(r.values()[1]['_key'].title, "Bug's Life, A (1998)")
        self.assertEqual(r.values()[2]['_value'], 39)
        self.assertEqual(r.values()[2]['_key'].title, 'Aladdin and the King of Thieves (1996)')
        self.assertEqual(r.values()[3]['_value'], 465)
        self.assertEqual(r.values()[3]['_key'].title, 'Chicken Run (2000)')
        self.assertEqual(r.values()[4]['_value'], 140)
        self.assertEqual(r.values()[4]['_key'].title, 'American Tail, An (1986)')
