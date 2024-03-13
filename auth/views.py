from django.shortcuts import redirect, render
from .forms import CreateUserForm, LoginUserForm

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import auth
# Create your views here.

def homepage(request):
    return render(request, 'homepage.html')

def profile(request):
    return render(request, 'profile.html')

def login(request):
    form = LoginUserForm()

    if request.method == 'POST':
        form = LoginUserForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']

            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)
                return redirect('/profile')
            
    context = {'loginform': form}
        
    return render(request, 'login.html', context=context)

def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')

    context = {'registerform': form}    

    return render(request, 'register.html', context=context)

def logout(request):
    auth.logout(request)

    return redirect('/')