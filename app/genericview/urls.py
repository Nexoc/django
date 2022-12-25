from django.urls import path, include
from .views import (HomeView, ThankYou, ContactFormView, 
                    ExampleCreateView, ExampleListView, ExampleDetailView,
                    ExampleUpdateView, ExampleDeleteView)

# python3 manage.py makemigrations
# python3 manage.py migrate

app_name = 'genericview'


urlpatterns = [
    path('',HomeView.as_view(),name='home'),
    path('thank_you/',ThankYou.as_view(),name='thank_you'),
    path('contact/',ContactFormView.as_view(),name='contact'),
    path('form/',ExampleCreateView.as_view(),name='create_form'),
    path('list/',ExampleListView.as_view(),name='list_form'),
    path('list/detail/<int:pk>/',ExampleDetailView.as_view(),name='detail_form'),
    path('list/update/<int:pk>/',ExampleUpdateView.as_view(),name='update_form'),
    path('list/delete/<int:pk>/',ExampleDeleteView.as_view(),name='delete_form'),
]
