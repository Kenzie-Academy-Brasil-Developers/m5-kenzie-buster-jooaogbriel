from . import views
from django.urls import path

urlpatterns = [
    path("movies/", views.MovieView.as_view()),
    path("movies/<movie_id>/", views.MovieDetailView.as_view()),
    path("movies/<movie_id>/orders/", views.MovieOrderDetailView.as_view()),
]