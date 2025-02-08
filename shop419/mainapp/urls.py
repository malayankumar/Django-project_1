from django.urls import path
from . import views
urlpatterns = [
    path("", views.homeView, name = "home"),
    path("about", views.aboutView, name = "aboutpage"),
    path("contacts", views.contactsView, name = "contactspage"),
]
