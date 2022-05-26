from django.db import models
#from django.forms import ModelForm

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length = 100, help_text = 'Project Name')
    creation_time = models.DateTimeField(auto_now_add = True, help_text = 'Creation Time')
    completion_time = models.DateTimeField(null= True, help_text = 'Completion time')

    def __str__(self):
        return self.name

class Task(models.Model):
    title = models.CharField(max_length = 100, help_text = 'Task Title')
    description = models.TextField(help_text = 'Task description')
    time_estimate = models.IntegerField(help_text = 'Estimated time')
    completed = models.BooleanField(default=False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

