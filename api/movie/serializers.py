# movie/serializer.py
from django.contrib.auth.models import User
from django.db.models import Avg, Count
from rest_framework import serializers
from .models import *



class FeedbackSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    

    class Meta:
        model = Feedback
        fields = ('id', 'user', 'discuss', 'rating')



class MovieListSerialzier(serializers.HyperlinkedModelSerializer):
    movie_url = serializers.HyperlinkedIdentityField(view_name='movie-detail', format='html')

    class Meta:
        model= Movies
        fields = ('id', 'title', 'year', 'movie_url')

class MovieSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    comments = serializers.StringRelatedField(many=True, read_only=True)


    class Meta:
        model = Movies

        fields = ('id', 'title', 'genre', 'director', 'producer', 'year', 'summary', 'owner', 'comments')



class UserListSerialziers(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'url')


class UserSerializer(serializers.HyperlinkedModelSerializer):

    movies= serializers.HyperlinkedRelatedField(many=True, view_name='movie-detail', read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username','movies')
