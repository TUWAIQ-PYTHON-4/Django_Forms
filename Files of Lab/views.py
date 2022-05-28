from django.shortcuts import render , get_object_or_404, redirect
from .models import Project, Task
from .import models
from .form import ProjectForm
from django.contrib import messages


def base(request):

    return render(request, "base.html")


def project(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, "project.html",context)


def task(request):
    context = Task.objects.all()
    return render(request, "task.html", {'context': context})

def AddProject(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
    else:
        form = ProjectForm()
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            for name, value in form.cleaned_data.items():
                print("{}: ({}) {}".format(name, type(value),value))
    return render(request, "addproject.html", {"method": request.method, "form": form})



 



