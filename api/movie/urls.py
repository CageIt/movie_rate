# movie/urls.py
from django.urls import path, re_path
from movie import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns=[
    path('', views.api_root),
    path('movies/', views.ListMoviesView.as_view(), name="movie-list"),
    path('movies/<int:pk>/', views.MoviesDetail.as_view(), name="movie-detail"),
    path('movie/review/<int:pk>/', views.ReviewList.as_view(), name="reviews"),
    path('movies/discussion/<int:pk>/', views.DiscussionList.as_view(), name="discussion-list"),
    path('users/', views.UserList.as_view(), name="user-list"),
    path('users/<int:pk>/', views.UserDetail.as_view(), name="user-detail"),

]
urlpatterns = format_suffix_patterns(urlpatterns)
