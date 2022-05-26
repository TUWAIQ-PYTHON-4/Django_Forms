from django.shortcuts import render
from .form import FormApp
from .form import ExampleForm


def form_app(request):
    form = FormApp()
    for name in request.POST:
        print("{}: {}".format(name, request.POST.getlist(name)))
    return render(request, "form_app2.html", {"method": request.method, "form": form})




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
    return render(request, "form_app2.html", {"method": request.method, "form": form})