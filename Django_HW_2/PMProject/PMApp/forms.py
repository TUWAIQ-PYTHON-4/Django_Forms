from django import forms

'''
class ExampleForm(forms.Form):
    user = forms.DecimalField(max_digits=8)
    password_input = forms.DecimalField(max_digits=8)
    project_name = forms.CharField(max_length=200, help_text="the name of the project")
    title = forms.CharField(max_length=200, help_text="the title of the task")
    description = forms.CharField(help_text="the description of the task")
    time_estimate = forms.IntegerField(help_text="the time estimate of the task")
'''

from .models import Task
class ExampleForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = "__all__"



