# movie/serializer.py
from django.contrib.auth.models import User
from django.db.models import Avg, Count
from rest_framework import serializers
from .models import *



class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    movie_id = serializers.ReadOnlyField(source='movie.id')

    class Meta:
        model = Discussions
        fields = ('id', 'discuss', 'movie_id','user')



class RatingSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source='owner.username')
    movie_id = serializers.ReadOnlyField(source='movie.id')

    class Meta:
        model = feedback
        fields = ('id', 'rating', 'movie_id', 'user')

class MovieListSerialzier(serializers.HyperlinkedModelSerializer):
    movie_url = serializers.HyperlinkedIdentityField(view_name='movie-detail', format='html')

    class Meta:
        model= Movies
        fields = ('id', 'title', 'year', 'movie_url')

class MovieSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    comments = serializers.StringRelatedField(many=True, read_only=True)
    ratings = serializers.ReadOnlyField(source='ratings.rating')

    rating_count = serializers.SerializerMethodField(read_only=True)
    rating_average = serializers.SerializerMethodField(read_only=True)

    def get_rating_count(self, obj):
        if ratings == 5:
            return obj.ratings.Count()
        elif ratings == 4:
            return obj.ratings.Count()
        elif ratings == 3:
            return obj.ratings.Count()
        elif ratings == 2:
            return obj.ratings.Count()
        elif ratings == 1:
            return obj.ratings.Count()

    def get_rating_average(self,obj):
        return obj.ratings.Avg()


    class Meta:
        model = Movies

        fields = ('id', 'title', 'genre', 'director', 'producer', 'year', 'summary', 'owner', 'comments', 'rating_avg', 'rating_count')



class UserListSerialziers(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'url')


class UserSerializer(serializers.HyperlinkedModelSerializer):

    movies= serializers.HyperlinkedRelatedField(many=True, view_name='movie-detail', read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username','movies')
