from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, FormView, CreateView, ListView, DetailView, UpdateView, DeleteView
from coctails_clean.forms import Cocktail
from coctails_clean.models import Coctail


class HomeView(TemplateView):
    template_name = 'coctails_clean/home.html'


class CoctailCreateView(CreateView):
    model = Coctail
    # form_class = Cocktail
    fields = "__all__"  # or ['name',"second_name"]
    success_url = reverse_lazy("coctails:list_form")


class CoctailListView(ListView):
    model = Coctail
    queryset = Coctail.objects.order_by("title")  # filtering
    context_object_name = "coctails_list"  # instead object


class CoctailDetailView(DetailView):
    model = Coctail


class CoctailUpdateView(UpdateView):
    model = Coctail
    fields = '__all__'  # ['last_name', 'first_name']
    success_url = reverse_lazy("coctails:list_form")


class CoctailDeleteView(DeleteView):
    # Form -> Confirm Delete Button
    # default template name:
    # model_confirm_delete.html
    model = Coctail
    success_url = reverse_lazy("coctails:list_form")
