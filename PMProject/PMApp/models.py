from django.db import models


# Create your models here.
from django.shortcuts import render


class Project(models.Model):
    name = models.CharField(max_length=50, help_text="The name of the project")
    creation_time = models.DateTimeField(auto_now_add=True, help_text="The creation time")
    completion_time = models.DateTimeField(null=True, help_text="The completion time")
    image_field = models.ImageField(upload_to="images/")

    def __str__(self):
        return self.name

def Project_list(request):
    project = Project.objects.all()
    Project_list = []
    for projects in project:
        Project_list.append({'project': projects})

    context = {'Publisher_list': Project_list}
    return render(request, 'index.html', context)


class Task(models.Model):
    title = models.CharField(max_length=50, help_text="The title")
    description = models.TextField(help_text="The description")
    time_estimate = models.IntegerField(help_text="the time estimate")
    completed = models.BooleanField(default=False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
