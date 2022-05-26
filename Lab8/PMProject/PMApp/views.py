from django.shortcuts import render
from .models import Task,Project
from .forms import ExampleForm, TaskForm


def home(request):
    form = TaskForm()
    x = Task.objects.all()
    context = []
    for i in x:
        context.append(i)
    return render(request,"home.html",{'context':context, "form":form})

def base(request):
    p = Project.objects.all()
    context = []
    for i in p:
        context.append(i)
    return render(request,'base.html',{'context':context})
def form(request):
    if request.method == "POST":
        form = ExampleForm(request.POST)
    else:
        form = ExampleForm()
    if request.method == "POST":
        form = ExampleForm(request.POST)
        if form.is_valid():
            for name, value in form.cleaned_data.items():
                print("{}: ({}) {}".format(name, type(value),value))
    return render(request, "form.html", {"method": request.method, "form": form})

