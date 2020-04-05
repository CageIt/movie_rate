from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import movie
from .serializers import MovieSerializer

# Create your tests here.
class BaseViewTest(APITestCase()):
    client = APIClient()

    @staticmethod
    def create_movie(title="", director=""):
        if title !="" and director != "":
            Movie.objects.create(title=title, director=director)

    def setUp(self):
        # add test data
        self.create_movie("Gozilla: King of the Monsters", "Michael Dougherty")
        self.create_movie("Avengers: Endgame", "Anthony Russo, Joe Russo")
        self.create_movie("Harry Potter and the Deathly Hallows - Part2", "David Yates")
        self.create_movie("Star Wars: The Rise of Skywalker", "J.J. Abrams")
        self.create_movie("Deadpool2", "David Leitch")
        self.create_movie("Underworld: Blood Wars", "Anna Foerster")
        self.create_movie("The Chronicles of Riddick", "David Twohy")
        self.create_movie("Kamen Rider Zi-O: Over Quartzer", "Ryuta Tasaki")
        self.create_movie("Bleach", "Shinsuke Sato")
        self.create_movie("Fantastic Beasts: The Crimes of Grindelwald", "David Yates")

class GetAllMoviesTest(BaseViewTest):
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
