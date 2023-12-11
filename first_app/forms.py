from django import forms
from django.forms.widgets import NumberInput
import datetime


class djangoForm(forms.Form):
    name = forms.CharField(max_length=30)
    comment = forms.CharField(widget=forms.Textarea)
    comment1 = forms.CharField(widget=forms.Textarea(attrs={'row': 3}))
    email = forms.EmailField()
    agree = forms.BooleanField()
    data = forms.DateField()
    birth_day = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
    BIRTH_CHOOSE = ['1980', '1970', '1990']
    birth_year = forms.DateField(
        widget=forms.SelectDateWidget(years=BIRTH_CHOOSE))
    email_addrres = forms.EmailField(
        required=False, label='Please enter your email address')
    first_name = forms.CharField(initial='Your name')
    today = forms.DateField(initial=datetime.date.today)
    FRUTS_CHOOSE = [
        ('banana', 'Banana'),
        ('papaya', 'Papaya'),
        ('painapple', 'Painapple'),
    ]
    furts = forms.ChoiceField(choices=FRUTS_CHOOSE)
    favarite_furts = forms.ChoiceField(
        widget=forms.RadioSelect, choices=FRUTS_CHOOSE)
    mlti_furst = forms.MultipleChoiceField(choices=FRUTS_CHOOSE)
    multi_fav = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple, choices=FRUTS_CHOOSE)
