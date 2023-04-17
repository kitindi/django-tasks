
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect

# Create your views here.



def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] =[]
        
    return render(request, 'index.html',{'tasks': request.session['tasks']} )

def add(request):
    
    if request.method == 'POST':
        task = request.POST['task']
        if task == '':
            error_message = 'Add task field'
            return render(request, 'add.html' , {'error_message': error_message})
        else:
            request.session["tasks"]+=[task]
            return HttpResponseRedirect(reverse('tasks:index'))
    
    return render(request, 'add.html' )