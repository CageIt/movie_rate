# movie/models.py
from django.db import models

# Create your models here.
class Movies(models.Model):
    # movie title
    title  = models.CharField(max_length=255, null=False)
    # name of the director(s)
    artist = models.CharField(max_length=255, null=False)

    def __str__(self):
        return "{} directed by {}".format(self.title, self.artist)
    
