from django.urls import path
from .import views

urlpatterns = [
    path('', views.enter),
    path('index', views.index),
    path('create', views.create_user),
    path('welcome',views.welcome),
    path('login', views.login),
    path('logout', views.logout),
     
]