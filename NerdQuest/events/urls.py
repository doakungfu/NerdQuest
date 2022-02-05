from django.urls import path
from . import views


urlpatterns = [
    path("allgames", views.all_games),
    path("games", views.games),
    path("games/new", views.new_game),
    # path("games/<int:game_id>", views.onegame), Kevin will do
    # path("games/<int:game_id>/edit>",views.edit ),David will do
    # path("games/<int:game_id/update", views.update),David will do
    # path("games/<int:game_id/delete", views.delete)
]