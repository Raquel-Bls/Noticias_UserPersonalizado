from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationFrom
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import TemplateView

# Create your views here.


class homePageview(TemplateView):
    template_name = 'home.html'


class SignUpView(generic.CreateView):
    form_class = CustomUserCreationFrom
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
