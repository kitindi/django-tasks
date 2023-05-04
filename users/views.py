from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, UserLoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
# Create your views here.

def signup(request):
    form = UserRegistrationForm()

    # if request.method == 'POST':
    #     username = request.POST['username']
    #     email = request.POST['email']
    #     password = request.POST['password1']
    #     confirm = request.POST['password2']

    #     if password == confirm:
    #         new_user = User.objects.create_user(username=username, email=email)
    #         new_user.set_password(password)
    #         new_user.save()
    #         return redirect('signin')

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, 'User created succesfully')
            return redirect('signin')

    
    context ={'form': form}
    return render(request, 'users/signup.html', context)

def signin(request):
    form = UserLoginForm()

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user =authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/profile/')

    context ={'form': form}
    return render(request, 'users/signin.html', context)
    

def signout(request):
    logout(request)

    return redirect('/')