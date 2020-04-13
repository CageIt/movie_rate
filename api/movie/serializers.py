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
    #owner = serializers.ReadOnlyField(source='owner.username')
    comments = serializers.StringRelatedField(many=True, read_only=True)
    all_rating = serializers.SerializerMethodField()
    rating_avg = serializers.SerializerMethodField()
    review_url = serializers.HyperlinkedIdentityField(view_name='review-list', format='html')



    class Meta:
        model = Movies

        fields = ('id', 'title', 'genre', 'director', 'producer', 'year', 'summary', 'review_url', 'rating_avg', 'all_rating', 'comments')


    def get_all_rating(self,obj):
        all_rating = {
            5 : obj.comments.filter(rating=5).count(),
            4 : obj.comments.filter(rating=4).count(),
            3 : obj.comments.filter(rating=3).count(),
            2 : obj.comments.filter(rating=2).count(),
            1 : obj.comments.filter(rating=1).count(),
        }
        return all_rating




    def get_rating_avg(self, obj):
        average = obj.comments.values('rating').aggregate(Avg('rating')).get('rating__avg')
        if average == 0:
            return 0
        return ("%.2f" % average)




class UserListSerialziers(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'url')


class UserSerializer(serializers.HyperlinkedModelSerializer):

    movies= serializers.HyperlinkedRelatedField(many=True, view_name='movie-detail', read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username','movies')
