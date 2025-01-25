from django.shortcuts import render, redirect
from .models import Noticia, Like
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

def login_vista(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect("home")
    else:
        form = AuthenticationForm()    
    return render(request, "usuarios/login.html", {"form": form})


def registrar(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            login(request, form.save())
            return redirect("home")
    else:
        form = UserCreationForm()
    return render(request, "usuarios/registrar.html", {"form": form})

def logout_vista(request):
    if request.method == "POST":
        logout(request)
        return redirect ("home")