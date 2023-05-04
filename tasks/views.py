from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import TaskCreationForm
from .models import Task

# Create your views here.


def home(request):
    return render(request, 'home.html')

@login_required(login_url='/signin/')
def profile(request):
    tasks = Task.objects.all()
    context = {'tasks':tasks}
        
    return render(request, 'profile.html', context)

@login_required(login_url='/signin/')
def add(request):
    form = TaskCreationForm()
    context ={'form':form}

    if request.method == 'POST':
        form = TaskCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/profile/')
    
    return render(request, 'add.html', context)

@login_required(login_url='/signin/')
def delete(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    return redirect('/profile/')

@login_required(login_url='signin/')
def edit(request,id):
    task = Task.objects.get(id=id)
    form = TaskCreationForm(instance=task)
    context ={'form':form}
    if request.method == 'POST':
        form = TaskCreationForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/profile/')
        
    return render(request, 'edit.html', {'form': form})