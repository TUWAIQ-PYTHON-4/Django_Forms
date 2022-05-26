from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=50, help_text="The name of project ")
    creation_time = models.DateTimeField(auto_now_add=True, help_text="Project creation time " )
    completion_time = models.DateTimeField(null=True, help_text="Completion time")
    #project_logo
    project_logo = models.ImageField(upload_to="images/")

    def __str__(self):
        return self.name

class Task(models.Model):

    project = models.ForeignKey('Project',on_delete=models.CASCADE,blank=True)
    title=models.CharField(max_length=50 , help_text="Task Title")
    description=models.TextField(help_text="Task description=")
    time_estimation=models.IntegerField(help_text="The task estimation time")
    completed=models.BooleanField(default=False)
