# movie/models.py
from django.db import models

# Create your models here.
class Movies(models.Model):

    # uploaded Date
    created = models.DateTimeField(auto_now_add=True)

    # movie title
    title  = models.CharField(max_length=255, null=False, blank=False)

    # name of the director(s)
    director = models.CharField(max_length=255,null=False, blank=False)
    # movie genre
    genre = models.CharField(null=True, blank=True, max_length=100)

    # name of the producer(s)
    producer = models.TextField(null=True ,blank=True)
    # release year
    year = models.CharField(max_length=4, null=True, blank=True)
    # summary
    summary = models.TextField(null=True, blank=True)
    # added by admin
    owner = models.ForeignKey('auth.User', related_name='movies', on_delete=models.CASCADE)

    #reviews  = models.ForeignKey('feedback', on_delete=models.SET_DEFAULT, null=True, default="NA" )
    #comments = models.ForeignKey('discussions', on_delete=models.SET_DEFAULT, null=True, default="NA")

    class Meta:
        ordering = ('created', )

    def __str__(self):
        return self.title



class Feedback(models.Model):

    SCORE_CHOICES = (
        (5, 5),
        (4, 4),
        (3, 3),
        (2, 2),
        (1, 1),
    )
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    movie = models.ForeignKey(Movies, related_name='comments', on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(choices=SCORE_CHOICES)
    status = models.BooleanField(default=True)
    discuss = models.TextField(blank=True)

    # uploaded Date
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created', )
        unique_together = ['movie', 'discuss']

    def __str__(self):
        return '{}: {} '.format(self.user, self.discuss)
