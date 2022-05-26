from django import forms
from .models import Project


class ExampleForm(forms.Form):
    user_name = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput())


class NewForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = "__all__"
