from django.db import models

class Project(models.Model):
    name = models.CharField(max_length = 110 , help_text = "The name of the Project.")
    creation_time = models.DateTimeField(auto_now_add=True , help_text="The is creatig time")
    completion_time = models.DateTimeField(null= True , help_text= "The is completion time")
    image_field = models.ImageField(upload_to="images/")

    def __str__(self):
        return self.name


class Task(models.Model):
    title = models.CharField(max_length= 110 , help_text= "The title of the Task.")
    description= models.TextField( help_text= "  ")
    time_estimate = models.IntegerField(help_text= "  ")
    completed = models.BooleanField(default = False)
    image_field = models.ImageField(upload_to="images/")
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


