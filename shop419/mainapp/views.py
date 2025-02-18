from django.shortcuts import render
from .models import Product
from django.http import HttpResponse
from django.template import loader
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from django.urls import reverse_lazy, reverse
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

class AddProduct(CreateView):
    model = Product
    fields = ['name', 'price', 'desc', 'pic', 'stock']
    template_name = 'addproduct.html'
    success_url = reverse_lazy('home')

#read
class ProductDetails(DetailView):
    model = Product
    template_name = 'prod_details.html'
    context_object_name = 'prod'

#update
class UpdateProduct(UpdateView):
    model = Product
    fields = '__all__'
    template_name = 'editproduct.html'
    def get_success_url(self):
        return reverse_lazy('prod_details', kwargs={'pk': self.object.pk})


#delete
class DeleteProduct(DeleteView):
    model = Product
    template_name = 'delproduct.html'
    success_url = reverse_lazy('home')

