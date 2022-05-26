from django import forms
from .models import Project, Task


class ExampleForm(forms.Form):
    name = forms.CharField(max_length=4, min_length=1)
    creation_time = forms.DateTimeField(required=True)


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = "__all__"


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = "__all__"
