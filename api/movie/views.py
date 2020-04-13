# movie/views
from django.contrib.auth.models import User
from django.shortcuts import render
from django.db.models import Count, Avg
from rest_framework import generics, permissions, renderers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.exceptions import ValidationError

from .models import *
from .permissions import *
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




class MoviesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movies.objects.all()
    serializer_class = MovieSerializer
    permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly|IsAuthenticatedAndReadOnly&permissions.IsAdminUser,)


class FeedbackList(generics.ListCreateAPIView):
    serializer_class = FeedbackSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    def get_queryset(self):
        token = self.kwargs['pk']
        query_set = Feedback.objects.filter(movie_id=token)
        return query_set







    def perform_create(self, serializer):


        if not Feedback.objects.filter(user=self.request.user).exists:
            serializer.save(
                user=self.request.user,
                movie_id = self.kwargs.get('pk'),
            )
        else:
            raise ValidationError('User already reviewed!')



class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerialziers
    permission_classes = (permissions.IsAuthenticated,)

class UserDetail(generics.RetrieveDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticatedAndReadOnly|permissions.IsAdminUser,)
