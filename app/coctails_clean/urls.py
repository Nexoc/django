from django.urls import path, include
from .views import (HomeView, CoctailCreateView, CoctailListView, 
                    CoctailDetailView, CoctailUpdateView, CoctailDeleteView)
from .views import coctail_create, success


# python3 manage.py makemigrations
# python3 manage.py migrate

app_name = 'coctails'


urlpatterns = [
    path('',HomeView.as_view(),name='home'),

    #path('create', coctail_create, name='create_form'),
    #path('success', success, name='success'),
    path('form/',CoctailCreateView.as_view(),name='create_form'),

    path('list/',CoctailListView.as_view(),name='list_form'),
    path('list/detail/<int:pk>/',CoctailDetailView.as_view(),name='detail_form'),
    path('list/update/<int:pk>/',CoctailUpdateView.as_view(),name='update_form'),
    path('list/delete/<int:pk>/',CoctailDeleteView.as_view(),name='delete_form'),
]


