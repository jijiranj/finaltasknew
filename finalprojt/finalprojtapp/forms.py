from django import forms
from django.core.validators import EmailValidator
from django.forms import SelectDateWidget


class RegistrationForm(forms.Form):
      name = forms.CharField(max_length=100)
      dob = forms.DateField(widget=SelectDateWidget(years=range(1930, 2029)))
      age = forms.IntegerField()
      gender = forms.ChoiceField(choices=[('male','Male'), ('female','Female'), ('transgender','Transgender')])
      phone_number = forms.CharField(max_length=15)
      email = forms.EmailField(validators=[EmailValidator()])
      password = forms.CharField(widget=forms.PasswordInput)
      address = forms.CharField(widget=forms.Textarea)
      # district = forms.ChoiceField(choices=[('calicut', 'Calicut'), ('cochin', 'Cochin'), ('kollam', 'Kollam'), ('kottayam', 'Kottayam'),('malappuram','Malappuram'),('palakad','Palakkad')])
      # branches = forms.ChoiceField([])
      account_type = forms.ChoiceField(choices=[('savings', 'Savings'), ('current', 'Current')])
      materials_required = forms.MultipleChoiceField(choices=[('debit', 'Debit Card'), ('credit', 'Credit Card'), ('cheque', 'Chequebook')], widget=forms.CheckboxSelectMultiple)

