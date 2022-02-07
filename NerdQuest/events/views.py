from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Game
from logreg.models import User
import bcrypt

 

def all_games(request):
    all_games=Game.objects.all()
    context = {
        'all_game': all_games
    }
    return render(request, 'events/all_games.html')

def one_game(request):
    context = {

    }
    return render(request, 'events/game.html', context)
def games(request):
     context = { 
         'my_games': Game.objects.all()
        #  'current_user': User.objects.filter(id=request.session['user_id'])
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
        gameType=request.POST['gameType'],
        date=request.POST['date'],
        startTime=request.POST['startTime'],
        endTime=request.POST['endTime'],
        location=request.POST['location'],
        creator = loggedin_user,
        notes=request.POST['notes']),
        
        
    return redirect('/games/')


 