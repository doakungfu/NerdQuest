from django.urls import path
from .import views

urlpatterns = [
    path('', views.index),
    path('user/create', views.create_user),
    path('user/login', views.login),
    path('user/logout', views.logout),
    path('success', views.success),
]