import datetime

from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=100, help_text="project name")
    creation_time = models.DateField(auto_now_add=True, help_text="Date of the Project .")
    completion_time = models.DateField(null=True, help_text="Completion time.")
    image_field = models.ImageField(upload_to="images/")
    project_logo=models.ImageField(upload_to="images/")

    def __str__(self):
        return self.name


class Task(models.Model):
    title = models.CharField(max_length=100, help_text="Task name")
    description = models.TextField(help_text="Task Help.")
    time_estimate = models.IntegerField(help_text="Task time.")
    completed = models.BooleanField(default=False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)#Relation
