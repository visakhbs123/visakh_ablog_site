from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from members.forms import SignUpForms
from theblog.models import Category


# Create your views here.

class UserRegisterView(generic.CreateView):
    form_class = SignUpForms
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(UserRegisterView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

