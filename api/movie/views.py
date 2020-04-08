# movie/views
from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import generics, permissions, renderers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from .models import Movies, Discussions
from .permissions import IsOwnerOrReadOnly
from .serializers import MovieSerializer, UserSerializer, CommentSerializer

# Create your views here.




@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'movies': reverse('movie-list', request=request, format=format),



    })

class ListMoviesView(generics.ListCreateAPIView):
    """
    Provides a get method handler
    """
    queryset = Movies.objects.all()
    serializer_class = MovieSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class MoviesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movies.objects.all()
    serializer_class = MovieSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)



class DiscussionList(generics.ListCreateAPIView):
    serializer_class = CommentSerializer(queryset, many=True)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    def get_queryset(self):
        token = self.kwargs['number']
        query_set = Discussions.objects.filter(movie=token)
        return query_set


    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
