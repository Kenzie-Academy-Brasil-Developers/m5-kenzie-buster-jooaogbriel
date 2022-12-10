from django.urls import path
from .views import UserView, UserLogin, UserDetailView

urlpatterns = [
    path("users/", UserView.as_view()),
    path("users/login/", UserLogin.as_view()),
    path("users/<user_id>/", UserDetailView.as_view()),
]