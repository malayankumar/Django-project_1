from django.urls import path

urlpatterns = [
    path("login", views.LoginView, name = "login"),
]
