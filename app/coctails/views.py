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


class CocktailCreate(CreateView):
    model = Coctail

    fields = [
        "title",
        "description",
        "price",
        "alcohol",
        "season",
        "type_of_drink",
    ]

    def get_initial(self):
        initial_data = super(CocktailCreate, self).get_initial()
        # cocktail_list = Coctail.objects.get(id=self.kwargs["cocktail_id"])
        # initial_data["cocktail_list"] = cocktail_list
        return initial_data

    def get_context_data(self):
        context = super(CocktailCreate, self).get_context_data()
        # cocktail_list = Coctail.objects.get(id=self.kwargs["list_id"])
        # context["cocktail_list"] = cocktail_list
        # context["title"] = "Create a new item"
        return context

    def get_success_url(self):
        return reverse("list", args=[self.object.cocktail_list_id])


class CocktailUpdate(UpdateView):
    model = Coctail
    fields = [
        "title",
        "description",
        "price",
        "created_date",
        "alcohol",
        "season",
        "type_of_drink",
    ]

    def get_context_data(self):
        context = super(CocktailUpdate, self).get_context_data()
        context["cocktail_list"] = self.object.cocktail_list_id
        context["title"] = "Edit item"
        return context

    def get_success_url(self):
        return reverse("list", args=[self.object.cocktail_list_id])

