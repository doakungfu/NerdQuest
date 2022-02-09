import re
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Game
# from logreg.models import User
# from django.contrib.auth.models import User
import bcrypt

 

def all_games(request):
    # all_games = Game.objects.all()

    context = {
       'my_games': Game.objects.all()
    }
    return render(request, 'events/all_games.html', context)

def my_games(request):
    context = {

         'my_games': Game.objects.all()
        #  'creator': User.objects.filter(id=request.session['user_id'])
    }     
    return render(request, 'events/my_games.html', context )


def new_game(request):

    return render(request, 'events/add_game.html')


def add_game(request):
    if request.method == 'POST':        
        # errors = Game.objects.create_validator(request.POST)
        # if len(errors) > 0 :
        #     for key, value in errors.items():
        #        messages.error(request, value)
        # return redirect('/games/new')
    
        # loggedin_user = User.objects.get(id=request.session["user_id"])
        Game.objects.create(
        gameType=request.POST['gameType'],
        date=request.POST['date'],
        startTime=request.POST['startTime'],
        endTime=request.POST['endTime'],
        location=request.POST['location'],
        # creator = loggedin_user,
        notes=request.POST['notes']),
        
        
    return redirect('/games/')

def one_game(request, game_id):
    context = {
        'game': Game.objects.get(id=game_id),
        # 'creator': User.objects.get(id=request.session['user_id'])
    }
    return render(request, 'events/game.html', context)

def edit(request, game_id):
    # one_game = Game.objects.get(id=show_id)
    context = {
        'game': Game.objects.get(id=game_id),
        # 'creator': User.objects.get(id=request.session['user_id'])
    }
    return render(request, 'events/edit_game.html', context)

def update(request, game_id):
    if request.method == 'POST':
        to_update = Game.objects.get(id=game_id)
        to_update.gameType = request.POST['gameType']
        to_update.date = request.POST['date']
        to_update.startTime = request.POST['startTime']
        to_update.endTime = request.POST['endTime']
        to_update.location = request.POST['location']
        to_update.notes = request.POST['notes']
        Game.save(game_id)
        
        return redirect('/games/')
        
def delete(request, game_id):
    to_delete = Game.objects.get(id=game_id)
    to_delete.delete()

    return redirect('/games/')