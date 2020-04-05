# movie/models.py
from django.db import models
from pygments import highlight
from pygments.formatters.html import HtmlFormatter
from pygments.lexers import get_all_lexers, get_lexer_by_name
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])
GENRE_CHOICES =(
                ('absuwh', 'Absurdist/surreal/whimsical'),
                ('action','Action'),
                ('adventure', 'Adventure'),
                ('anime', 'Animation'),
                ('comedy', 'Comedy'),
                ('crime', 'Crime'),
                ('drama', 'Drama'),
                ('fantasy', 'Fantasy'),
                ('historical', 'Historical'),
                ('historicalf', 'Historical fiction'),
                ('horror', 'Horror'),
                ('magical','Magical realism'),
                ('mystery', 'Mystery'),
                ('paranoid', 'Paranoid fiction'),
                ('philosophical', 'Philosophical'),
                ('political', 'Political'),
                ('puppetry', 'Puppetry'),
                ('romance', 'Romance'),
                ('saga', 'Saga'),
                ('staire', 'Satire'),
                ('science', 'Science Fiction'),
                ('social', 'Social'),
                ('speculative', 'Speculative'),
                ('thriller', 'Thriller'),
                ('urban', 'Urban'),
                ('western', 'Western'),
)



# Create your models here.
class Movies(models.Model):

    # uploaded Date
    created = models.DateTimeField(auto_now_add=True)

    # movie title
    title  = models.CharField(max_length=255, null=False, blank=False)
    # movie genre
    genre = models.CharField(choices= GENRE_CHOICES, default='Action', max_length=100)
    # name of the director(s)
    director = models.CharField(max_length=255, null=False, blank=False)
    # name of the producer(s)
    producer = models.TextField(blank=True)
    # release year
    year = models.CharField(max_length=4, null=True, blank=True)
    # summary
    summary = models.TextField(blank=True)
    # added by admin
    owner = models.ForeignKey('auth.User', related_name='movies', on_delete=models.CASCADE)
    # URL for  movie detail
    highlighted = models.TextField()

    class Meta:
        ordering = ('created', )
        


    def __str__(self):
        return '{} directed by {} '.format(self.title, self.director)
