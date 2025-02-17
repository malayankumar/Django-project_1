from django.urls import path
from . import views
urlpatterns = [
    path("", views.homeView, name = "home"),
    path("about", views.aboutView, name = "aboutpage"),
    path("products/add", views.AddProduct.as_view(), name = "addproduct"),
    path("Products/int<pk>", views.ProductDetails.as_view(), name = "prod_details"),
    path("Products/edit/<int:pk>", views.UpdateProduct.as_view(), name = "editproduct"),
    path("Products/del/<int:pk>", views.DeleteProduct.as_view(), name = "delproduct"),
]
