from django.urls import path
from . import views


urlpatterns = [
<<<<<<< HEAD
    path("games/all", views.all_games),
=======
    path("allgames", views.all_games),
>>>>>>> 8ae3bf1a8beb472fa8a074fede0d5ce1464870c2
    path("games", views.games),
    path("games/new", views.new_game),
    # path("games/<int:game_id>", views.onegame), Kevin will do
    # path("games/<int:game_id>/edit>",views.edit ),David will do
    # path("games/<int:game_id/update", views.update),David will do
    # path("games/<int:game_id/delete", views.delete)
]