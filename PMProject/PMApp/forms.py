
'''
 from django import forms

class TaskForm(forms.Form):
    text_input = forms.CharField()
    text_area = forms.CharField(widget=forms.Textarea)
    integer_input = forms.IntegerField()
    checkbox_on = forms.BooleanField()

'''

from django import forms
from .models import Task
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = "__all__"
