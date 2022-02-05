from importlib.resources import read_text
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Game
from logreg.models import User
import bcrypt

 

def all_games(request):
    return render(request, 'events/all_games.html')


def games(request):
     context = {

         
         'my_games': Game.objects.all()
 
     }
     return render(request, 'events/games.html', context )


def new_game(request):

    return render(request, 'events/add_game.html')


def add_game(request):
    if request.method == 'POST':        
        # errors = Game.objects.create_validator(request.POST)
        # if len(errors) > 0 :
        #     for key, value in errors.items():
        #        messages.error(request, value)
        # return redirect('/games/new')
    
        loggedin_user = User.objects.get(id=request.session["user_id"])
        Game.objects.create(
        type=request.POST['title'],
        date=request.POST['date'],
        start=request.POST['start'],
        end=request.POST['end'],
        location=request.POST['end'],
        notes=request.POST['notes'])
    return redirect('/games/')


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
