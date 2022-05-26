"""from django import forms
RADIO_CHOICES = (
("Value One", "Creation"),
("Value Two", "Updated"),
("Value Three", "Completed")
)
PROJECT_CHOICES = (
("COMPLETED", (("1", "LAB 1"), ("2", "LAB 2"))),
("NON-COMPLETE", (("3", "LAB 3"),("4", "LAB 4")))
)
class ExampleForm(forms.Form):
    decimal_input = forms.DecimalField(max_digits=3)
class ExampleForm(forms.Form):
    User = forms.CharField()
    Password = forms.CharField(min_length=8, widget=forms.PasswordInput)
    #Checkbox_on = forms.BooleanField()
    What_do_you_want_to_do = forms.ChoiceField(choices=RADIO_CHOICES, widget=forms.RadioSelect)
    Choose_your_project = forms.ChoiceField(choices=PROJECT_CHOICES)
    #Project_you_own = forms.MultipleChoiceField(choices=PROJECT_CHOICES)
    Project_description = forms.CharField(widget=forms.Textarea)
    Number_of_people_in_the_project = forms.IntegerField(min_value=1, max_value=10)
    #float_input = forms.FloatField()
    The_cost_of_the_project = forms.DecimalField(max_digits=5, decimal_places=3)
    Email = forms.EmailField()
    Project_date= forms.DateField(widget=forms.DateInput(attrs={"type": "date"}))
    #hidden_input = forms.CharField(widget=forms.HiddenInput, initial="Hidden Value")"""

from django import forms
from .models import Task
class  ExampleForm(forms.ModelForm):
        class Meta:

            model = Task
            fields = "__all__"