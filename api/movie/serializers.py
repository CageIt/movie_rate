# movie/serializer.py
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Movies

class MovieSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='movie-highlight', format='html')

    class Meta:
        model = Movies
        fields = ('id', 'highlight', 'title', 'genre', 'director', 'producer', 'year', 'owner')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    movies = serializers.HyperlinkedRelatedField(many=True, view_name='movie-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'movies')
