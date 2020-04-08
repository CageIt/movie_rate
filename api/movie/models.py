# movie/models.py
from django.db import models

# Create your models here.
class Movies(models.Model):

    # uploaded Date
    created = models.DateTimeField(auto_now_add=True)

    # movie title
    title  = models.CharField(max_length=255, null=False, blank=False)
    # movie genre
    genre = models.CharField(null=True, blank=True, max_length=100)
    # name of the director(s)
    director = models.CharField(max_length=255,null=False, blank=False)
    # name of the producer(s)
    producer = models.TextField(null=True ,blank=True)
    # release year
    year = models.CharField(max_length=4, null=True, blank=True)
    # summary
    summary = models.TextField(null=True, blank=True)
    # added by admin
    owner = models.ForeignKey('auth.User', related_name='movies', on_delete=models.CASCADE)

    #rating  = models.ForeignKey('reviews', on_delete=models.SET_DEFAULT, null=True, default="NA" )
    comments = models.ForeignKey('discussions', related_name='movies',on_delete=models.SET_DEFAULT, null=True, blank=True, default="NA")

    class Meta:
        ordering = ('created', )

    def __str__(self):
        return '{} directed by {} '.format(self.title, self.director)



class Discussions(models.Model):


    user = models.ForeignKey('auth.User', related_name='discussions', on_delete=models.CASCADE)
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE, null=True, blank=True)
    discuss = models.TextField(blank=True)

    


    def __str__(self):
        return '{} commented on {}'. format(self.user, self.movie)
