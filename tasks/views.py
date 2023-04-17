
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect

# Create your views here.
tasks = []


def index(request):
    return render(request, 'index.html', {'tasks': tasks})

def add(request):
    
    if request.method == 'POST':
        task = request.POST['task']
        tasks.append(task)
        return HttpResponseRedirect(reverse('tasks:index'))
    
    return render(request, 'add.html' )