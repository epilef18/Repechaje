from django.urls import path
from . import views

app_name = "usuarios"

urlpatterns = [
    path("login/", views.login_vista, name="login"),
    path("logout/", views.logout_vista, name="logout"),
    path("registrar/", views.registrar, name="registrar"),
]
