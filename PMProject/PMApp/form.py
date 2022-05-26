from django import forms
from .models import Project

class ExampleForm(forms.Form):
    name = forms.CharField(max_length=4, min_length=1)
    creation_time = forms.DateTimeField(required=True)

class NewForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = "__all__"