from django.shortcuts import render
from .models import Task, Project

from .forms import TaskForm

# Create your views here.

def task_form(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
    else:
        form = TaskForm()
    if request.method == "POST":
        form = TaskForm(request.POST)
    if form.is_valid():
        for name, value in form.cleaned_data.items():
            print("{}: ({}) {}".format(name, type(value),value))
    return render(request, "taskform.html", {"method": request.method, "form": form})


def project_object(request):
    project_objects = Project.objects.all()

    context = {'project':project_objects}

    return render(request, 'project.html', context)


def project_tasks_object(request):
    tasks_objects = Task.objects.all()

    context = {'task':tasks_objects}

    return render(request, 'tasks.html', context)




