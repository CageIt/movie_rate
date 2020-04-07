# movie/serializer.py
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Movies, Reviews, Discussions

class MovieSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Movies
        fields = ('id', 'title', 'genre', 'director', 'producer', 'year', 'summary', 'owner')

class RatingSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Reviews
        fields = ('rating', 'movie', 'user')

class CommentSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')


    class Meta:
        model = Discussions
        fields = ('comment', 'movie', 'user')

class UserSerializer(serializers.HyperlinkedModelSerializer):


    class Meta:
        model = User
        fields = ('url', 'id', 'username')
