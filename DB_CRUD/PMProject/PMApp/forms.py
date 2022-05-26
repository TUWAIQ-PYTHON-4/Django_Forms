from django import forms
from django import forms
from .models import Task

RADIO_CHOICES = (
    ("Value One", "Value One Display"),
    ("Value Two", "Text For Value Two"),
    ("Value Three", "Value Three's Display Text")
)
MOVIE_CHOICES = (
    ("Non-Fiction", (("1", "Movie X"), ("2", "Movie Z"))),
    ("Fiction", (("3", "Movie A"), ("4", "Movie B")))
)


class ExampleForm(forms.Form):
    text_input = forms.CharField(max_length=3)
    password_input = forms.CharField(min_length=8, widget=forms.PasswordInput)
    movies_you_own = forms.MultipleChoiceField(required=False, choices=MOVIE_CHOICES)
    integer_input = forms.IntegerField(min_value=1, max_value=10)
    decimal_input = forms.DecimalField(max_digits=5, decimal_places=3)
    email_input = forms.EmailField()
    date_input = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}))
    hidden_input = forms.CharField(widget=forms.HiddenInput, initial="Hidden Value")


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
