from django import forms
from .models import Project


class project_form(forms.ModelForm):

    class Meta:
        model = Project
        fields = ['name']
    