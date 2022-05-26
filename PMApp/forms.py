from django import forms

from .models import Task

class taskrForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = "__all__"

class PMForm(forms.Form):
    title = forms.CharField()
    completed = forms.BooleanField()
    description = forms.CharField(widget=forms.Textarea)
    time_estimate = forms.IntegerField(max_value=6 , min_value= 1)
