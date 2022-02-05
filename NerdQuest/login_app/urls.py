from django.urls import path
from .import views

urlpatterns = [
    path('', views.enter),
    path('user/index', views.index),
    path('user/create', views.create_user),
    path('user/welcome',views.welcome),
    path('user/login', views.login),
    path('user/logout', views.logout),
     
]