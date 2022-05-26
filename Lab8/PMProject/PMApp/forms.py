from django import forms
from .models import Task
RADIO_CHOICES = (
    ("Value One", "Yearly"),
    ("Value Two", "Monthly"),
    ("Value Three", "Weekly"),
    ("Value Four", "No repeat")
)


class ExampleForm(forms.Form):
    Project_name = forms.CharField(min_length=6)
    Manager_of_project = forms.CharField(max_length=50)
    checkbox_on = forms.BooleanField(required=False)
    repeat = forms.ChoiceField(choices=RADIO_CHOICES, widget=forms.RadioSelect)
    Tasks_area = forms.CharField(widget=forms.Textarea)
    Daily_hours = forms.FloatField()
    email_input = forms.EmailField()
    date_input = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}))
    hidden_input = forms.CharField(widget=forms.HiddenInput, initial="Hidden Value")


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = "__all__"
