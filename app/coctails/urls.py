from django.urls import path
from . import views


app_name = 'coctails'
# app name: path name
# return redirect(reverse('coctails:create'))
urlpatterns = [
    path("", views.CocktailsListView.as_view()),
    path("create/", views.create_new_coctail, name='create'),
    path("thank_you/", views.thank_you, name='thanks'),
]