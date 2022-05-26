from django.shortcuts import render
from .form import *
from .models import Project


def Index_viwes(request):
    image=Project.objects.all()
    return render(request,"base.html",{'image':image })

def form_example(request):
    if request.method == "POST":
        form = ExampleForm(request.POST)
    else:
        form = ExampleForm()
    if request.method == "POST":
        form = ExampleForm(request.POST)
        if form.is_valid():
            for name, creation_time in form.cleaned_data.items():
                print("{}: ({}) {}".format(name, type(creation_time),creation_time))
    return render(request, "example.html", {"method": request.method, "form": form})