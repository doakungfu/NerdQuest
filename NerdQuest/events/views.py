from pydoc import importfile
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
import bcrypt   


def index(request):
    return render(request, 'workouts/index.html')

def register(request):
    errors = User.objects.register_validator(request.POST)

    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        user = User.objects.create(
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            email = request.POST['email'],
            password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
        )
        request.session['user_id'] = user.id
        request.session['greeting'] = user.first_name
        return redirect('/workouts')

def login(request):
    errors = User.objects.login_validator(request.POST)

    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        user = User.objects.get(email=request.POST['login_email'])
        request.session['user_id'] = user.id
        request.session['greeting'] = user.first_name
        return redirect('/workouts')

def logout(request):
    request.session.flush()

    return redirect('/')

def all_games(request):
     
    context = {
        'all_games': Game.objects.exclude(created_by='user.first.name')
    }
    return render(request, 'all_games.html', context)

def games(request):
    context = {
       'games' : Game.objects.filter(created_by='user.first.name')
    }
