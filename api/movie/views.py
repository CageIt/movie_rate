# movie/views
from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import generics, permissions, renderers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from .models import *
from .permissions import IsOwnerOrReadOnly
from .serializers import *
# Create your views here.
@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'movies': reverse('movie-list', request=request, format=format),
    })

class ListMoviesView(generics.ListAPIView):
    """
    Provides a get method handler
    """
    queryset = Movies.objects.all()
    serializer_class = MovieListSerialzier


class MoviesDetail(generics.RetrieveAPIView):
    queryset = Movies.objects.all()
    serializer_class = MovieSerializer

class DiscussionList(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    def get_queryset(self):
        token = self.kwargs['pk']
        query_set = Discussions.objects.filter(movie_id=token)
        return query_set


    def perform_create(self, serializer):
        serializer.save(
            user=self.request.user,
            movie_id = self.kwargs.get('pk'),
        )


class ReviewList(generics.ListCreateAPIView):
    serializer_class = RatingSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        token = self.kwargs['pk']
        queryset = feedback.objects.filter(movie_id=token)
        return queryset

    def perform_create(self, serializer):
        serializer.save(
            user=self.request.user,
            movie_id = self.kwargs.get('pk'),
        )

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerialziers

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
