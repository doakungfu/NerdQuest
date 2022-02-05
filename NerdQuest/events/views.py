from importlib.resources import read_text
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
import bcrypt






# # log in and registration page
# def index(request):
#     context = {}
#     return render(request, 'index.html', context)
# 
    # this is the page that has the 3 buttons
# def welcome(request):, 
#     return render(request,'welcome.html')
# 
# def register(request):
#     if request.method != "POST":
#         return redirect('/index')
#     errors = User.objects.register_validator(request.POST)
#     if len(errors) > 0:
#         for key, value in errors.items():
#             messages.error(request, value)
#         return redirect('/index')
#    
#     
#     new_user = User.objects.create(
#         first_name=request.POST['first_name'],
#         last_name=request.POST['last_name'],
#         email=request.POST['email'], 
#         hashed_pw = bcrypt.hashpw(request.POST['password'].encode(),bcrypt.gensalt(14)).decode()
#         password=hashed_pw
#     )
#         #store users id in session
#     request.session['user_id'] = new_user.id
#     request.session['first_name'] = new_user.first_name
#   q
# def all_games(request):

#     context = {
#         'all_games': Game.objects.exclude(created_by='user.first.name')
#     }
#     return render(request, 'all_games.html', context)


def all_games(request):
    return render(request, 'events/all_games.html')


def games(request):
     
    return render(request, 'events/games.html' )


def add_game(request):
    return render(request, 'events/add_game.html')


def new_game(request):
    if request.method == 'POST':
      errors = Game.objects.create_validator(request.POST)
      if len(errors) > 0 :
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/games/new')
    
        new_user = User.objects.get(id=request.session["user_id"])
        new_game = Game.objects.create(
        type=request.POST['title'],
        date=request.POST['date'],
        start=request.POST['start'],
        end=request.POST['end'],
        location=request.POST['end'],
        notes=request.POST['notes'],
        creator= Game.objects.get(id= request.session['user_id'])
    )
    return redirect('/games')


# def create(request):
    # CREATE THE SHOW
#     errors = Show.objects.validate(request.POST)
#     if errors:
#         for (key, value) in errors.items():
#             messages.error(request, value)
#         return redirect('/shows/new')
#
#     Show.objects.create(
#         title = request.POST['title'],
#         network = request.POST['network'],
#         release_date = request.POST['release_date'],
#         description = request.POST['description']
#     )
#     return redirect('/shows')
