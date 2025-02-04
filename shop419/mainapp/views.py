from django.shortcuts import render
from .models import Product
# Create your views here.
def homeView(request):
    products = Product.objects.all()
    context ={
        'product_list': products
    }
    return 