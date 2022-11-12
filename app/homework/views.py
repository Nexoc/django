from django.shortcuts import render
from django.views.generic import TemplateView
from .models import HomeWork  # from homework.models


def home(request, *args, **kwargs):
    m_list = HomeWork.objects.all()
    my_list = ["eins", "zwei", "drei"]
    return render(request, 'html/home.html', {"name_von_my_list": m_list})


class About(TemplateView):
    template_name = 'html/about.html'

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
    return render(request, 'html/ip.html', {'ip_address': ip, 'host': host})  # with variables
