from django.db import models


# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=100, help_text="The name of the project.")
    creation_time = models.DateTimeField(auto_now_add=True, help_text="Date the project was created.")
    completion_time = models.DateTimeField(null=True, help_text="Date the project was completed.")
    image_field = models.ImageField(upload_to="images/")

    def __str__(self):
        return self.name


class Task(models.Model):
    title = models.CharField(max_length=100, help_text='Task Title')
    description = models.TextField(help_text='Task description')
    time_estimate = models.IntegerField(help_text=' Task estimated time')
    completed = models.BooleanField(default=False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.title + ' ' + self.description + ' ' + str(self.time_estimate) + ' ' + str(self.completed)
