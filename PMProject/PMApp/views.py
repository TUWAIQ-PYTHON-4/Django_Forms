from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import project_form
from .models import Project
from django.contrib import messages


def home_view(request):
    #form = project_form()
    #for name in request.POST:
        #print('{}: {}'.format(name,request.POST.getlist(name)))
        #return render(request, 'home.html', {'method': request.method, 'form':form})

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = project_form(request.POST)
        # check whether it's valid:
        if form.is_valid():
            for name, value in form.cleaned_data.items():
                print("{}: ({}) {}".format(name,type(value), value))
            #project_form.save()
            #messages.success(request, ('Your movie was successfully added!'))
        #else:
            #messages.error(request, ('Error saving form'))

        #return redirect("home.html")
    else:
        form = project_form()

    #project = Project.objects.all()
    return render(request, 'home.html', {'method': request.method, 'form':form}) 
