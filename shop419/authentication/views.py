from django.shortcuts import render,redirect
from django.url import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView

class UserRegistration(createview):
    form_class = UserCreationForm
    template_name = 'register.html'
    success_url = reverse_lazy('signin')
# Create your views here.
class Login(LoginView):
    template_name = 'login.html'

