from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name='index'),
    path("home/", views.home, name='index'),
    path("about/", views.About.as_view()),
    path("ip/", views.get_client_ip, name='ip'),
    path("homework/", views.HomeWorkListView.as_view(), name='homework_list'),
    path("homework/<int:pk>", views.HomeWorkDetailView.as_view(), name='homework-detail'),
]
