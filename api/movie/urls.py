# movie/urls.py
from django.urls import path
from movie import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns=[
    path('movies/', views.ListMoviesView.as_view(), name="movie-list"),
    path('movies/<int:pk>/', views.ListMoviesDetail.as_view(), name="movie-detail"),
    path('movies/<int:pk>/highlight/', views.MovieHighlight.as_view(), name="movie-highlight"),
    path('users/', views.UserList.as_view(), name="user-list"),
    path('users/<int:pk>/', views.UserDetail.as_view(), name="user-detail"),
    path('', views.api_root, name="")
]
urlpatterns = format_suffix_patterns(urlpatterns)
