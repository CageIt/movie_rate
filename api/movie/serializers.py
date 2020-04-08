# movie/serializer.py
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Movies, Discussions

class CommentSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    #movie = serializers.ReadOnlyField(source='movie.title')

    class Meta:
        model = Discussions
        fields = ('id', 'discuss', 'user')


class MovieSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    comments = CommentSerializer(many=True, read_only=True)
    class Meta:
        model = Movies

        fields = ('id', 'title', 'genre', 'director', 'producer', 'year', 'summary', 'owner', 'comments')





class UserSerializer(serializers.HyperlinkedModelSerializer):

    movies= serializers.HyperlinkedRelatedField(many=True, view_name='movie-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username','movies')
