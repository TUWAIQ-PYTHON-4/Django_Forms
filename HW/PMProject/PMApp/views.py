from django.shortcuts import render
from .models import Task


def home(request):
    x = Task.objects.all()
    context = []
    for i in x:
        context.append(i)
    return render(request, "home.html", {'context': context})


def form_example(request):
    return render(request, "form-example.html")



