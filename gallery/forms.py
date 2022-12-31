from django import forms
from django.forms import (CharField, EmailField)
from django_countries.fields import CountryField



#class CheckoutForm(forms.Form):
    #address = forms.CharField(widget=forms.TextInput(attrs={
    #'placeholder':'building 1234, villa 34, road 6543'
    #}))
    #country = CountryField(blank_label='(select country)')
    #save_address = forms.BooleanField(widget=forms.CheckboxInput())
    #payment_options = forms.ChoiceField(widget=forms.RadioSelect,choices=PAYMENT_CHOICE)
