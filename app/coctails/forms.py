from .models import Coctail
from django import forms
# manage.py shell


class Cocktail(forms.ModelForm):

    class Meta:
        model = Coctail
        fields = '__all__'  # fields = [title, price]
        exclude = ['created_date']

        labels = {
            'title':'Title',
            'description': 'Description',
            'price': 'Price',
            'alcohol': 'Alcohol',
            'season': 'Season',
            'type_of_drink': 'Type of drink',
        }

        error_messages = {
            'price':{
                'min_value':'Hei, Mimumus is 1',
                'max_value':'Hei Yasin! Maximus is just 15',
            },
        }