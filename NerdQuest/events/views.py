from pydoc import importfile
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, Game
import bcrypt


# Landing page to nerdquest
# def enter(request):
# return render(request,'enter.html')

# log in and registration page
def index(request):
    return render(request, 'index.html')

    # this is the page that has the 3 buttons
# def welcome(request):
#     return render(request,'welcome.html')


def register(request):
    if request.method == "GET":
        return redirect('/index')
    errors = User.objects.validate(request.POST)
    if errors:
        for e in errors.values():
            messages.error(request, e)
        return redirect('/')
        #     else:
        new_user = User.objects.create(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            email=request.POST['email'],
            password=bcrypt.hashpw(
            request.POST['password'].encode(), bcrypt.gensalt()).decode()
        )
        request.session['user_id'] = user.id
        request.session['greeting'] = user.first_name
        return redirect('/allgames')


def login(request):
     if request.method == 'POST':
     

    # if len(errors):
    #     for key, value in errors.items():
    #         messages.error(request, value)
    #     return redirect('/')
    # else:
        user = User.objects.get(email=request.POST['login_email'])
        request.session['user_id'] = user.id
        request.session['greeting'] = user.first_name
        return redirect('/allgames')


def logout(request):
    request.session.flush()

    return redirect('/')

# def all_games(request):

#     context = {
#         'all_games': Game.objects.exclude(created_by='user.first.name')
#     }
#     return render(request, 'all_games.html', context)


def all_games(request):
    return render(request, 'all_games.html')


def games(request):
    context = {
        'games': Game.objects.filter(created_by='user.first.name')
    }
    return render(request, 'games.html', context)


def new_game(request):
    return render(request, 'add_game.html')


def new_game(request):
    if request.method == 'POST':
      errors = Game.objects.create_validator(request.POST)
      if len(errors) > 0 :
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/games/new')
    else:
        new_user = User.objects.get(id=request.session["user_id"])
        new_game = Game.objects.create(
        type=request.POST['title'],
        date=request.POST['date'],
        start=request.POST['start'],
        end=request.POST['end'],
        location=request.POST['end'],
        notes=request.POST['notes'],
        creator= Game.objects.get(id= request.session[user_id])
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
