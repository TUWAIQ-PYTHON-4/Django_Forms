from django.shortcuts import render
from . import models
from .forms import ExampleForm

# Create your views here.

def index(request):
    context = models.Project.objects.all()
    return render(request, 'index.html',{"context":context})

def forms(request):
    if request.method == "POST":
        form = ExampleForm(request.POST)
    else:
        form = ExampleForm()
    if request.method == "POST":
        form = ExampleForm(request.POST)
    if form.is_valid():
        for name, value in form.cleaned_data.items():
            print("{}: ({}) {}".format(name, type(value),value))
    return render(request, "forms.html", {"method": request.method, "form": form})


