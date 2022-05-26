from django.shortcuts import render
from .models import Project
from .forms import forms
from .forms import ExampleForm


# Create your views here.

def Pmp(request):
    return render(request, 'home.html', {})


def project_list(request):
    project = Project.objects.all()
    project_list = []

    for project in project:
        project_list.append({'project': project})

    context = {'project_list': project_list}
    return render(request, 'home.html', context)


# def form_example(request):
#     form = ExampleForm()
#     for name in request.POST:
#         print("{}: {}".format(name, request.POST.getlist(name)))
#     return render(request, "home.html", {"method": request.method, "form": form})


# def form_example(request):
#     for name in request.POST:
#         print("{}: {}".format(name, request.POST.getlist(name)))
#     return render(request, "home.html", {"method": request.method})


def form_example(request):
    if request.method == "POST":
        form = ExampleForm(request.POST)
    else:
        form = ExampleForm()
    if request.method == "POST":
        form = ExampleForm(request.POST)
        if form.is_valid():
            for name, value in form.cleaned_data.items():
                print("{}: ({}) {}".format(name, type(value), value))
    return render(request, "home.html", {"method": request.method, "form": form})
