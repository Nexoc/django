from django.shortcuts import render
from django.views import generic
from django.views.generic import TemplateView
from .models import HomeWork  # from homework.models


def home(request, *args, **kwargs):
    m_list = HomeWork.objects.all()[:5]  # first 5
    # my_list = ["eins", "zwei", "drei"]
    return render(request, 'home.html', {"name_von_my_list": m_list})


class About(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = "Marat"
        context['title'] = "title"
        context['description'] = """
        Man kann alles schreiben, was man will!
        """
        return context


# https://docs.djangoproject.com/en/4.1/ref/request-response/
def get_client_ip(request):
    ip = request.META.get('REMOTE_ADDR')  # REMOTE_ADDR – The IP address of the client.
    host = request.META.get('HTTP_HOST')  # HTTP_HOST – The HTTP Host header sent by the client.
    # (url=f'http://ip-api.com/json/{ip}')
    return render(request, 'ip.html', {'ip_address': ip, 'host': host})  # with variables


class HomeWorkListView(generic.ListView):
    model = HomeWork
    template_name = "homework_list.html"
    context_object_name = "homework_list"  # rename
    queryset = HomeWork.objects.all()


class HomeWorkDetailView(generic.DetailView):
    model = HomeWork
    # template_name = "homework_detail.html"  # /templates/homework/homework_detail.html
