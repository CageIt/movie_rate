# api/test.py
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import Movies
from .serializers import MoviesSerializer

# Create your tests here.
class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_movie(title="", director="", producer="", year=""):
        if title !="" and director != "":
            Movies.objects.create(title=title, director=director, producer=producer, year=year)

    def setUp(self):
        # add test data
        self.create_movie("Gozilla: King of the Monsters", "Michael Dougherty", "Marry Parent, Alex Garcia, Thomas Tull, Jon Jashni, Brian Rogers", "2019")
        self.create_movie("Avengers: Endgame", "Anthony Russo, Joe Russo", "Kevin Feige", "2019")
        self.create_movie("Harry Potter and the Deathly Hallows - Part2", "David Yates", "David Heyman, David Barron, J.K. Rowling", "2011")
        self.create_movie("Star Wars: The Rise of Skywalker", "J.J. Abrams", "Kathleen Kennedy, J.J. Abrams, Michelle Rejwan", "2019")
        self.create_movie("Deadpool2", "David Leitch", "Simon Kinberg, Ryan Reynolds, Lauren Shuler Donner", "2016")
        self.create_movie("Underworld: Blood Wars", "Anna Foerster", "Tom Rosenberg, Len Wiseman, Richard Wright, David Kern", "2016")
        self.create_movie("The Chronicles of Riddick", "David Twohy", "Scott Kroopf, Vin Diesel", "2004")
        self.create_movie("Kamen Rider Zi-O: Over Quartzer", "Ryuta Tasaki", "", "2019")
        self.create_movie("Bleach", "Shinsuke Sato", "Shinsuke Sato, Disuke Habara", "2018")
        self.create_movie("Fantastic Beasts: The Crimes of Grindelwald", "David Yates", "David Heyman, J.K. Rowling, Steve Kloves, Lionel Wigram", "2018")

class GetAllMoviesTest(BaseViewTest):

    def test_all_movies(self):
        """
        This test ensures that all movies added in the setUp method
        exist when we make a GET request to the movies.
        """
        #hit the API endpoint
        response = self.client.get(
            reverse("movies-all", kwargs={"version": "v1"})
        )

        # fetch the data from database
        expected = Movies.objects.all()
        serialized = MoviesSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
