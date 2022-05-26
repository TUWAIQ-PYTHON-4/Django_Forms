from django.shortcuts import render
from PMApp.models import Task, Project
from .forms import ExampleForm

def project(request):
    proj = Project.objects.all()
    project = []
    for P in proj:
        project.append({'P': P})
    context = {'project': project}
    return render(request, "base.html", context)


def lst():
    Task.objects.all()
    context = {"key1": "value", "key2": "value"}
    return context


def form_example(request):
    if request.method == "POST":
        form = ExampleForm(request.POST)
    else:
        form = ExampleForm()
    if request.method == "POST":
        form = ExampleForm(request.POST)
        if form.is_valid():
            for name, value in form.cleaned_data.items():
                print("{}: ({}) {}".format(name, type(value),value))
    return render(request, "form-example.html", {"method": request.method, "form": form})