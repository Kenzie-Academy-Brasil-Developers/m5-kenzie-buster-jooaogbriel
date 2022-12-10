from django.urls import path
from .views import MovieView, MovieDetailView, MovieOrderDetailView

urlpatterns = [
    path("movies/", MovieView.as_view()),
    path("movies/<movie_id>/", MovieDetailView.as_view()),
    path("movies/<movie_id>/orders/", MovieOrderDetailView.as_view()),
]