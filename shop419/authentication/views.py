from django.shortcuts import render,redirect
from django.url import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm

def UserRegistration(createview):
    form_class = UserCreationForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

# Create your views here.
