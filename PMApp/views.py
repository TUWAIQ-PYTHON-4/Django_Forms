from django.shortcuts import render
from .forms import PMForm
# Create your views here.
from .models import Task


def admin_object(request):
    if request.method == "POST":
        form = PMForm(request.POST)
    else:
        form = PMForm()

    if request.method == "POST":
        form = PMForm(request.POST)
    if form.is_valid():
        for name, value in form.cleaned_data.items():
            print("{}: ({}) {}".format(name, type(value), value))

    x = Task.objects.all()
    Tasks = []
    for i in x:
        Tasks.append(i)

    for name in request.POST:
        print("{}: {}".format(name, request.POST.getlist(name)))

    return render(request, "base.html", {"Tasks": Tasks, 'method':request.method  })

def form (request):
    if request.method == "POST":
        form = PMForm(request.POST)
    else:
        form = PMForm()

    if request.method == "POST":
        form = PMForm(request.POST)
    if form.is_valid():
        for name, value in form.cleaned_data.items():
            print("{}: ({}) {}".format(name, type(value), value))

    return render(request, 'form.html' , {'form':form})

