# movie/models.py
from django.db import models

# Create your models here.
class Movies(models.Model):
    # movie title
    title  = models.CharField(max_length=255, null=False)
    # name of the director(s)
    director = models.CharField(max_length=255, null=False)
    # name of the producer(s)
    producer = models.CharField(max_length=255, null=True)
    # release year
    year = models.CharField(max_length=4, null=True)


    def __str__(self):
        return "{} directed by {} , produced by {} ,and release in {}".format(self.title, self.director, self.producer, self.year)
