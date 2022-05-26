from django.shortcuts import render
from .forms import ExampleForm
from .models import Publisher


def index(request):
    context = Publisher.Project.objects.all()
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
    return render(request, "base.html", {"method": request.method, "form": form})

