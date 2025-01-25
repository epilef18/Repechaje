from django.urls import path
from . import views

app_name = "cotizacion"

urlpatterns = [
    path("cotizar/", views.cotizar, name="cotizar"),
    path("cotizacion/", views.cotizacion, name="cotizacion"),
]
