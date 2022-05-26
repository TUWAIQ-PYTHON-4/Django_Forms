from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=100, help_text="The name of the project.")
    creation_time = models.DateTimeField(auto_now_add=True, help_text="The creation time of the project.")
    completion_time = models.DateTimeField(null=True, help_text="The completion time of the project.")
    project_logo = models.ImageField(upload_to="images/")
    def __str__(self):
        return self.name


class Task(models.Model):
    title = models.CharField(max_length=150, help_text="The title of the task.")
    description = models.TextField(help_text="The description of task.")
    time_estimate = models.IntegerField(help_text="The time estimate of task.")
    completed = models.BooleanField(default=False)
    project = models.ForeignKey('Project', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
