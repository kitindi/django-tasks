
from django.shortcuts import render, redirect
from .forms import TaskCreationForm
from .models import Task

# Create your views here.



def index(request):
    tasks = Task.objects.all()
    context = {'tasks':tasks}
        
    return render(request, 'index.html', context)

def add(request):
    form = TaskCreationForm()
    context ={'form':form}

    if request.method == 'POST':
        form = TaskCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    
    return render(request, 'add.html', context)