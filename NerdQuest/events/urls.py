from django.urls import path
from . import views


urlpatterns = [
    path("", views.index),
    path("register", views.register),
    path("login", views.login),
    path("logout", views.logout),
    path("allgames", views.all_games),
    path("games", views.games),
    # path("game/create", views.create_game),
    path("games/new", views.new_game),


]