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
    template = loader.get_template('mainapp/home.html')
    return HttpResponse(templates.render(context, request))