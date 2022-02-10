from django.shortcuts import render, redirect
import bcrypt
from .models import *
from django.contrib import messages


def enter(request):
    return render(request, 'enter.html')

def index(request):
    return render(request, 'index.html')



def create_user(request):
    if request.method == "POST":
        errors = User.objects.create_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/index')
        else:
            password = request.POST['password']
            pw_hash = bcrypt.hashpw(
                password.encode(), bcrypt.gensalt()).decode()
            user = User.objects.create(
                first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=pw_hash)
            request.session['user_id'] = user.id
            return redirect('/welcome')
    return redirect('/index')



def login(request):
    if request.method == "POST":
        users_with_email = User.objects.filter(email=request.POST['email'])
        if users_with_email:
            user = users_with_email[0]
            if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
                request.session['user_id'] = user.id
                return redirect('/welcome')
        messages.error(request, "Email or password is incorrect")
    return redirect('/index')



def welcome(request):
    if 'user_id' not in request.session:
        return redirect('/index')
    context = {
        'current_user': User.objects.get(id=request.session['user_id'])
    }
    return render(request, 'welcome.html', context)



def logout(request):
    request.session.flush()
    return redirect('/')

def all_games(request):
    # all_games = Game.objects.all()

    context = {
       'my_games': Game.objects.all()
    }
    return render(request, 'all_games.html', context)

def my_games(request):
    context = {

         'my_games': Game.objects.all()
        #  'creator': User.objects.filter(id=request.session['user_id'])
    }     
    return render(request, 'my_games.html', context )


def new_game(request):

    return render(request, 'add_game.html')


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
    return render(request, 'game.html', context)

def edit(request, game_id):
    # one_game = Game.objects.get(id=show_id)
    context = {
        'game': Game.objects.get(id=game_id),
        # 'creator': User.objects.get(id=request.session['user_id'])
    }
    return render(request, 'edit_game.html', context)

def update(request, game_id):
    if request.method == 'POST':
        to_update = Game.objects.get(id=game_id)
        to_update.gameType = request.POST['gameType']
        to_update.date = request.POST['date']
        to_update.startTime = request.POST['startTime']
        to_update.endTime = request.POST['endTime']
        to_update.location = request.POST['location']
        to_update.notes = request.POST['notes']
        # Game.save(game_id)
        
        return redirect('/games/')
        
def delete(request, game_id):
    to_delete = Game.objects.get(id=game_id)
    to_delete.delete()

    return redirect('/games/')