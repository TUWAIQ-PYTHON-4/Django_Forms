from django.shortcuts import render

from django.shortcuts import render
from . import models
from .forms import ExampleForm


# Create your views here.
def home(request):
    context = models.Project.objects.all()
    return render(request, "home.html", {'context': context})

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
    return render(request, "form_example.html", {"method": request.method, "form": form})
