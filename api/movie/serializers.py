# movie/serializer.py
from django.contrib.auth.models import User
from django.db.models import Avg, Count
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from .models import *



class FeedbackSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.id')
    #movie_id = serializers.ReadOnlyField(source='movie.id')

    class Meta:
        model = Feedback

        fields = ('id', 'user', 'rating', 'discuss')



class MovieListSerialzier(serializers.HyperlinkedModelSerializer):
    movie_url = serializers.HyperlinkedIdentityField(view_name='movie-detail', format='html')

    class Meta:
        model= Movies
        fields = ('id', 'title', 'year', 'movie_url')

class MovieSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    comments = serializers.StringRelatedField(many=True, read_only=True)
    rating = serializers.SerializerMethodField()

    

    class Meta:
        model = Movies

        fields = ('id', 'title', 'genre', 'director', 'producer', 'year', 'summary', 'owner', 'rating', 'comments')

    def get_rating(self, obj):
        rating = Feedback.objects.values('rating').annotate(rate_count=Count('rating'))
        return rating



class UserListSerialziers(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'url')


class UserSerializer(serializers.HyperlinkedModelSerializer):

    movies= serializers.HyperlinkedRelatedField(many=True, view_name='movie-detail', read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username','movies')
