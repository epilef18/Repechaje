from django.shortcuts import render


def cotizar(request):
    return render(request, "cotizacion/cotizar.html", {})


def cotizacion(request):
    return render(request, "cotizacion/cotizacion.html", {})
