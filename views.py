from django.shortcuts import render
from .form import *
from . import models# models


# Create your views here.
def index(request):
    context = models.Task.objects.all()# models
    return render(request, 'home.html', {'context': context})# templets

def form_example(request):
  form = ProjectForm()
  if request.method == "POST":
      form = ProjectForm(request.POST)
  else:
      form = ProjectForm()
  if request.method == "POST":
      form = ProjectForm(request.POST)
  if form.is_valid():
      for name, value in form.cleaned_data.items():
          print("{}: ({}) {}".format(name, type(value),value))
  return render(request, "form-example.html", {"method": request.method, "form": form})

  return render(request, "form-example.html", {"method": request.method, "form": form})
