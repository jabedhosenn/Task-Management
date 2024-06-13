from django.shortcuts import render, redirect
from .forms import TaskForm
from .models import TaskModel


# Create your views here.
def addTask(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = TaskForm()
    return render(request, "task/add_task.html", {"form": form})


def deleteTask(request, id):
    task = TaskModel.objects.get(pk=id)
    task.delete()
    return redirect("home")


def updateTask(request, id):
    task = TaskModel.objects.get(pk=id)
    form = TaskForm(instance=task)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("home")
    return render(request, "task/add_task.html", {"form": form})
