from django.shortcuts import render
from .models import Product
from django.http import HttpResponse
from django.template import loader
# Create your views here.
def homeView(request):
    products = Product.objects.all()
    context ={
        'product_list': products
    }
    template = loader.get_template('home.html')
    return HttpResponse(template.render(context, request))

def aboutView(request):
    context = {
        'name': "Ayan",
        'students': [
            "Varun",
            "Harsha",
            "Srikanth",
        ],
        'slept':  False,

    }
    template = loader.get_template('about.html')
    return HttpResponse(template.render(context, request))

def contactsView(request):
    context = {

    }
    template = loader.get_template('contacts.html')
    return HttpResponse(template.render(context, request))