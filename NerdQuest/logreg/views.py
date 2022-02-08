from django.shortcuts import render, redirect
import bcrypt
from .models import User
from django.contrib import messages


# Create your views here.
# Landing page to nerdquest


def enter(request):
    return render(request, 'logreg/enter.html')

def index(request):
    return render(request, 'logreg/index.html')



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
    return render(request, 'logreg/welcome.html', context)

def upload_avatar(request):
    if request.method == "POST" or request.method == "FILES":
        pass

def logout(request):
    request.session.flush()
    return redirect('/')
 