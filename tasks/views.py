from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import TaskCreationForm
from .models import Task
from django.contrib.auth.models import User

# Create your views here.


def home(request):
    return render(request, "home.html")


@login_required
def profile(request):
    tasks = Task.objects.filter(author=request.user)
    context = {"tasks": tasks, "user": request.user.username}

    return render(request, "profile.html", context)


@login_required
def add(request):
    form = TaskCreationForm()
    context = {"form": form}

    if request.method == "POST":
        task_form = TaskCreationForm(request.POST)
        if task_form.is_valid():
            # add user to the instance ↓
            # task_form = form.save(commit=False)
            task_form.instance.author = request.user
            task_form.save()

            return redirect("/profile/")

    return render(request, "add.html", context)


@login_required
def delete(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    return redirect("/profile/")


@login_required
def edit(request, id):
    task = Task.objects.get(id=id)
    form = TaskCreationForm(instance=task)
    context = {"form": form}
    if request.method == "POST":
        form = TaskCreationForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("/profile/")

    return render(request, "edit.html", {"form": form})
