"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from coctails.views import CocktailsListView, CocktailCreate, CocktailUpdate
from profiles.views import UserFormView, UserEditFormView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('homework.urls')),
    path('profiles/', include('profiles.urls')),
    path('profiles/register/', UserFormView.as_view()),
    path('profiles/show/', UserFormView.as_view()),
    path('profiles/<int:profile_id>/edit/', UserEditFormView.as_view()),

    path("cocktails/", CocktailsListView.as_view(), name="was ist das? app/urls"),
    # path("list/<int:list_id>/", cocktails.CocktailsListView.as_view(), name="list"),
    # path('cocktails/', include('coctails.urls')),
    # CRUD patterns for create new cocktail
    path(
        "cocktails/create/",
        CocktailCreate.as_view(),
        name="cocktail-add",
    ),
    path(
        "cocktails/<int:list_id>/item/<int:pk>/",
        CocktailUpdate.as_view(),
        name="cocktail-update",
    ),
]
