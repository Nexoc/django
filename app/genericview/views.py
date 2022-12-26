from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, FormView, CreateView, ListView, DetailView, UpdateView, DeleteView
from genericview.forms import ContactForm
from genericview.models import GDatabase
# dir temp is templates/genericview/home.html


# def home_view(request):
#    return render(request, 'genericview/home.html')
class HomeView(TemplateView):
    template_name = 'genericview/home.html'


class ThankYou(TemplateView):
    template_name = 'genericview/thank_you.html'


class ExampleCreateView(CreateView):
    model = GDatabase
    # model_form.html 
    # .save()
    fields = "__all__"  # or ['first_name',"second_name"]
    success_url = reverse_lazy("genericview:thank_you")


class ExampleListView(ListView):
    # model_list.html
    model = GDatabase
    # queryset = GDatabase.objects.all()  # by default
    queryset = GDatabase.objects.order_by("first_name")  # filtering
    context_object_name = "example_list"  # instead object


class ExampleDetailView(DetailView):
    # model_detail.html
    model = GDatabase
    # PK -> {{ example }}


class ExampleUpdateView(UpdateView):
    # Return Only One Model entry PK -> PK
    # model_detail.html
    model = GDatabase
    fields = '__all__'  # ['last_name', 'first_name']
    success_url = reverse_lazy("genericview:list_form")


class ExampleDeleteView(DeleteView):
    # Form -> Confirm Delete Button
    # default template name:
    # mpdel_confirm_delete.html
    model = GDatabase
    success_url = reverse_lazy("genericview:list_form")


class ContactFormView(FormView):
    form_class = ContactForm
    template_name = "genericview/contact.html"

    # succcess URL is URL and is NOT template.html
    # success_url = "/genericview/thank_you/"
    success_url = reverse_lazy("genericview:thank_you")

    # what to do with form
    def form_valid(self,form):
        # form.save()
        print(form.cleaned_data)
        # it is like: ContactForm(request.POST)
        return super().form_valid(form)



