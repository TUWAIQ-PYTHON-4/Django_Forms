from django import forms
RADIO_CHOICES = (("Value One", "Value One Display"),("Value Two", "Text For Value Two"),("Value Three", "Value Three's Display Text"))
MOVIE_CHOICES = (("Non-Fiction", (("1", "Movie X"), ("2", "Movie Z"))),("Fiction", (("3", "Movie A"),("4", "Movie B"))))
class ExampleForm(forms.Form):
    text_input = forms.CharField()
    password_input = forms.CharField(widget=forms.PasswordInput)
    checkbox_on = forms.BooleanField()
    radio_input = forms.ChoiceField(choices=RADIO_CHOICES, widget=forms.RadioSelect)
    favorite_movie = forms.ChoiceField(choices=MOVIE_CHOICES)
    movies_you_own = forms.MultipleChoiceField(choices=MOVIE_CHOICES)
    text_area = forms.CharField(widget=forms.Textarea)
    integer_input = forms.IntegerField()
    float_input = forms.FloatField()
    decimal_input = forms.DecimalField()
    email_input = forms.EmailField()
    date_input = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}))
    hidden_input = forms.CharField(widget=forms.HiddenInput, initial="Hidden Value")

