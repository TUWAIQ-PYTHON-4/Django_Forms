from django.shortcuts import render
from .models import Task
from .forms import PMForm

# Create your views here.
def index(request):
    task = Task.objects.all()
    taskList = []

    for t in task:
        taskList.append({'task': t})
    context = {'taskList': taskList}
    return render(request, 'home.html', context)

def base(request):
    return render(request, 'base.html')

def home(request):
    if request.method == "POST":
        form = PMForm(request.POST)
    else:
        form = PMForm()
    if request.method == "POST":
        form = PMForm(request.POST)
    if form.is_valid():
        for name, value in form.cleaned_data.items():
            print("{}: ({}) {}".format(name, type(value), value))
    return render(request, "home.html", {"method": request.method, "form": form})


