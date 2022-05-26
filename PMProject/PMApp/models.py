from django.db import models


class Project(models.Model):
   name = models.CharField(max_length=100, help_text="The name of the Project.")
   creation_time = models.DateTimeField(auto_now_add=True, help_text = "The date and time the project was created.")
   completion_time = models.DateTimeField(null=True, help_text="The date and time the project was completed.")
   image= models.ImageField(upload_to="images/")

   def __str__(self):
      return self.name

class Task(models.Model):
   title = models.CharField(max_length=100, help_text="The Title of the Task.")
   description = models.TextField(help_text = "The description of the Task.")
   time_estimate = models.IntegerField(help_text="The estimate for the Task.")
   completed = models.BooleanField(default=False)
   project = models.ForeignKey(Project, on_delete=models.CASCADE)
   def __str__(self):
      return self.title