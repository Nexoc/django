from django.shortcuts import render,redirect
from .models import Coctail
from django.urls import reverse
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView
)
from .forms import Cocktail

# DBname.objects.get() -> 1 object; .all()[:5] -> all first 5; .filter(last_name='smith').all
# from django.db.models import Q # -> AND OR
# Coctail.objects.filter(Q(price=4)& Q(title='margarita')).all()  # AND &
# Coctail.objects.filter(Q(price=4)| Q(title='margarita')).all()  # OR  |
# filter(title__startswith='s').all()  # startswith
# filter(price__in=[1, 5, 15, 20]).all()  # in 
# filter(price__gte=6).all()  # gte gr or equel; gte, lt, lte, 
# Coctail.objects.filter((price=4).order_by('title').all()


class CocktailsListView(ListView):
    model = Coctail  # From DB
    template_name = "coctails.html"
    context_object_name = "cocktail_list"  # rename
    queryset = Coctail.objects.all()


def create_new_coctail(request):
    if request.method == 'POST':
        form = Cocktail(request.POST)  # From Form

        if form.is_valid():
            # print(form.cleaned_data)
            form.save()
            return redirect(reverse('coctails:create'))

    else:
        form = Cocktail()

    return render(request, "create.html", context={'form':form})


def thank_you(request):
    return render(request, 'thank_you.html')





