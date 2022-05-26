class ExampleForm(forms.Form):
decimal_input = forms.DecimalField(max_digits=3)
text_input = forms.CharField(max_length=3)
password_input = forms.CharField(min_length=8, widget=forms.Pa
sswordInput)
movies_you_own = forms.MultipleChoiceField(required=False, cho
ices=MOVIE_CHOICES)
integer_input = forms.IntegerField(min_value=1, max_value=10)
decimal_input = forms.DecimalField(max_digits=5, decimal_place
s=3)