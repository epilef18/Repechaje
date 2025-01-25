from django.urls import path
from . import views

app_name = "usuarios"

urlpatterns = [
    path("login/", views.login, name="login"),
    path("registrar/", views.registrar, name="registrar"),
]
