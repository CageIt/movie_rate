# movie/serializer.py
from django.contrib.auth.models import User
import django.contrib.auth.password_validation as validation
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
    ratings = serializers.SerializerMethodField()

    review_url = serializers.HyperlinkedIdentityField(view_name='review-list', format='html')



    class Meta:
        model = Movies

        fields = ('id', 'title', 'genre', 'director', 'producer', 'year', 'summary', 'review_url', 'ratings', 'comments')


    def get_ratings(self,obj):
        average =  obj.comments.values('rating').aggregate(Avg('rating')).get('rating__avg')
        if average == None:
            return {
                'average': 0,
                'rate at 5': 0,
                'rate at 4' : 0,
                'rate at 3' : 0,
                'rate at 2' : 0,
                'rate at 1' : 0,
            }
        all_rating = {
            'average': ("%.2f" % average),
            'rate at 5': obj.comments.filter(rating=5).count(),
            'rate at 4' : obj.comments.filter(rating=4).count(),
            'rate at 3' : obj.comments.filter(rating=3).count(),
            'rate at 2' : obj.comments.filter(rating=2).count(),
            'rate at 1' : obj.comments.filter(rating=1).count(),
        }
        return all_rating

class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email')
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        user = User.objects.create_user(
            username = validated_data['username'],
            password = validated_data['password'],
            email = validated_data['email'],
        )
        return user




class UserListSerialziers(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'url')


class UserSerializer(serializers.HyperlinkedModelSerializer):

    movies= serializers.HyperlinkedRelatedField(many=True, view_name='movie-detail', read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username','movies')
