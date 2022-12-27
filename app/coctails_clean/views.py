from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, FormView, CreateView, ListView, DetailView, UpdateView, DeleteView
from coctails_clean.forms import Cocktail
from coctails_clean.models import Coctail
from django.http import HttpResponse


class HomeView(TemplateView):
    template_name = 'coctails_clean/home.html'



def coctail_create(request):
    if request.method == 'POST':
        form = Cocktail(request.POST, request.FILES)
        if form.is_valid:
            form.save()
            return redirect('success')
    else:
        form = Cocktail()
    return render(request, 'coctail_form.html', {'form': form})

def success(request):
    return HttpResponse("successfully uploaded")



class CoctailCreateView(CreateView):
    model = Coctail
    form_class = Cocktail
    success_url = reverse_lazy("coctails:list_form")


class CoctailListView(ListView):
    model = Coctail
    queryset = Coctail.objects.order_by("title")  # filtering
    context_object_name = "coctails_list"  # instead object


class CoctailDetailView(DetailView):
    model = Coctail


class CoctailUpdateView(UpdateView):
    model = Coctail
    form_class = Cocktail
    # fields = '__all__'  # ['last_name', 'first_name']
    success_url = reverse_lazy("coctails:list_form")


class CoctailDeleteView(DeleteView):
    # Form -> Confirm Delete Button
    # default template name:
    # model_confirm_delete.html
    model = Coctail
    success_url = reverse_lazy("coctails:list_form")
