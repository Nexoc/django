from django.shortcuts import render
from .models import Coctail
from django.urls import reverse
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
)


# Create your views here:
class CocktailsListView(ListView):
    model = Coctail
    template_name = "coctails.html"
    context_object_name = "cocktail_list"  # rename
    queryset = Coctail.objects.all()
