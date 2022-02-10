from django.urls import path
from .import views

urlpatterns = [
    path('', views.enter),
    path('index', views.index),
    path('create', views.create_user),
    path('welcome',views.welcome),
    path('login', views.login),
    path('logout', views.logout),
    path('all', views.all_games),
    path('games/', views.my_games),
    path('games/new', views.new_game),
    path('games/add', views.add_game),
    path('games/<int:game_id>', views.one_game),
    path('games/<int:game_id>/edit',views.edit),
    path('games/<int:game_id>/update', views.update),
    path('games/<int:game_id>/delete', views.delete)
     
]