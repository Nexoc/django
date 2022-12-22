from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UserForm
from django.views import View
from .models import User


def show(request, *args, **kwargs):
    m_list = User.objects.all()  # [:5]  # first 5
    return render(request, "profiles/show.html", {"name_von_my_list": m_list})


class UserFormView(View):

    def get(self, request):
        user_form = UserForm()
        return render(request, "profiles/register.html", context={"user_form": user_form})

    def post(self, request):
        user_form = UserForm(request.POST)

        if user_form.is_valid():
            # do something, save in DB
            User.objects.create(**user_form.cleaned_data)
            return HttpResponseRedirect('/')
        return render(request, "profiles/register.html", context={"user_form": user_form})


class UserEditFormView(View):

    def get(self, request, profile_id):
        user = User.objects.get(id=profile_id)
        user_form = UserForm(instance=user)
        print(f'user get: {user.id} - {profile_id}')
        return render(request, 'profiles/edit.html', context={'user_form': user_form, 'profile_id': profile_id})

    def post(self, request, profile_id):
        print(f'user post: - > {profile_id}')
        user = User.objects.get(id=profile_id)
        user_form = UserForm(request.POST, instance=user)

        if user_form.is_valid():
            user.save()
        return render(request, 'profiles/edit.html', context={'user_form': user_form, 'profile_id': profile_id})
