# movie/views
from django.contrib.auth.models import User
from django.shortcuts import render
from django.db.models import Count, Avg
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



class FeedbackList(generics.ListCreateAPIView):
    serializer_class = FeedbackSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    def get_queryset(self):
        token = self.kwargs['pk']
        query_set = Feedback.objects.filter(movie_id=token)
        return query_set

    rate_count_dict = Feedback.objects.values('rating').annotate(rate_count=Count('rating'))

    #rate_avg = Feedback.objects.values('rating').annotate(avg=Avg('rating'))

    def perform_create(self, serializer):
        queryset = Feedback.objects.filter(user=self.request.user)
        if not queryset.exists():
            serializer.save(
                user=self.request.user,
                movie_id = self.kwargs.get('pk'),
            )




class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerialziers
    permission_classes = (permissions.IsAuthenticated,)

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAdminUser,)
