from django.shortcuts import render

# Create your views here.


def home(request, *args, **kwargs):
    my_list = ["eins", "zwei", "drei"]
    return render(request, 'html/home.html', {"name_von_my_list": my_list})


def about(request):
    return render(request, 'html/about.html', {})


# https://docs.djangoproject.com/en/4.1/ref/request-response/
def get_client_ip(request):
    ip = request.META.get('REMOTE_ADDR')  # REMOTE_ADDR – The IP address of the client.
    host = request.META.get('HTTP_HOST')  # HTTP_HOST – The HTTP Host header sent by the client.
    # (url=f'http://ip-api.com/json/{ip}')
    return render(request, 'html/ip.html', {'ip_address': ip, 'host': host})  # with variables
