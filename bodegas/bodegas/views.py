from usuarios.models import Noticia
from django.shortcuts import render

def home(request):
    noticias = Noticia.objects.all()
    return render(request, "home.html", {"noticias": noticias})