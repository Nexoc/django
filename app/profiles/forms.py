from django import forms
from django.core.exceptions import ValidationError
# manage.py shell



class UserForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    # birthday = forms.DateField()  # 2010-01.10

    def clean_user(self):
        user = self.cleaned_data['username']  #

        if user == "Marat" or user == 'marat':
            raise ValidationError('Your name is not Marat. Please enter your name again')
        return user

    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')
        if first_name == 'Marat' and last_name == 'Davletshin':
            msg = 'You are not Marat Davletshin. Enter your name correctly'
            self.add_error('first_name', msg)
            self.add_error('last_name', msg)

