from .models import Coctail
from django import forms
# manage.py shell


class Cocktail(forms.ModelForm):

    class Meta:
        model = Coctail
        fields = '__all__'
        # exclude = ['title']