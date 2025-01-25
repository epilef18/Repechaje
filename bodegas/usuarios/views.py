from django.shortcuts import render, redirect
from .models import Noticia, Like
from django.contrib.auth.forms import UserCreationForm

def login(request):
    return render(request, "usuarios/login.html")


def registrar(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("usuarios:home")
    else:
        form = UserCreationForm()
    return render(request, "usuarios/registrar.html", {"form": form})
