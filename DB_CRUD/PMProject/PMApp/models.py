from django.db import models


# Create your models here.
def __str__(self):
    return self.name


class Project(models.Model):
    name = models.CharField(max_length=100, help_text="The Project Name")
    creation_time = models.DateTimeField(auto_now_add=True, help_text="The creation time")
    completion_time = models.DateTimeField(null=True, help_text="The completion time")

    def __str__(self):
        return self.name


class Task(models.Model):
    title = models.CharField(max_length=100, help_text="The title Name")
    description = models.TextField(help_text="The description Name")
    time_estimate = models.IntegerField(help_text="The estimate time")
    completed = models.BooleanField(default=False)
    Project = models.ForeignKey(Project, on_delete=models.CASCADE)


def __str__(self):
    return self.title
