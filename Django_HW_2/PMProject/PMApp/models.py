from django.db import models


# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=100, help_text="the name of the Project")
    creation_time = models.DateTimeField(auto_now_add=True, help_text="the creation time of the Project")
    completion_time = models.DateTimeField(null=True, help_text="the completion time of the Project")
    image_field = models.ImageField(upload_to="images/")

    def __str__(self):
        return self.name


class Task(models.Model):
    title = models.CharField(max_length=200, help_text="the title of the task")
    description = models.TextField(help_text="the description of the task")
    time_estimate = models.IntegerField(help_text="the time estimate of the task")
    completed = models.BooleanField(default=False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
