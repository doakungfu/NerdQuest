from django.shortcuts import render,redirect
import bcrypt
from login_app.models import User
from django.contrib import messages

# Create your views here.
# Landing page to nerdquest
def enter(request):
    return render(request,'login/enter.html')

def index(request):
    return render(request, 'login/index.html')

def create_user(request):
    if request.method == "POST":
        errors = User.objects.create_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        else:
            password = request.POST['password']
            pw_hash = bcrypt.hashpw(
                password.encode(), bcrypt.gensalt()).decode()
            user = User.objects.create(
                first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=pw_hash)
            request.session['user_id'] = user.id
            return redirect('/success')
    return redirect('/')

def login(request):
    if request.method == "POST":
        users_with_email = User.objects.filter(email=request.POST['email'])
        if users_with_email:
            user = users_with_email[0]
            if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
                request.session['user_id'] = user.id
                return redirect('/success')
        messages.error(request, "Email or password is incorrect")
    return redirect('/success')

def welcome(request):
    if 'user_id' not in request.session:
        return redirect('/')
    context = {
        'current_user': User.objects.get(id=request.session['user_id'])
    }
    return render(request, 'loging/welcome.html', context)

def logout(request):
    request.session.flush()
    return redirect('/')    
 