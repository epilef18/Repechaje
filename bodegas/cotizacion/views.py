from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CotizacionForm
from .models import TipoBodega, Bodega, Cotizacion

@login_required
def cotizar(request):
    seleccionadas = request.session.get('bodegas_seleccionadas', [])
    if "agregar" in request.POST:  
            form = CotizacionForm(request.POST)
            if form.is_valid():
                bodega = form.cleaned_data['tipo_bodega']
                seleccionadas.append(bodega.id)
                request.session['bodegas_seleccionadas'] = seleccionadas
                return redirect("cotizacion:cotizar")
    elif "cotizar" in request.POST:  
        cotizacion = Cotizacion(usuario=request.user)
        cotizacion.save()
        bodegas = Bodega.objects.filter(id__in=seleccionadas)
        cotizacion.bodegas.set(bodegas)
        cotizacion.calcular_total()
        request.session['bodegas_seleccionadas'] = []
        return render(request, "cotizacion/cotizacion.html", {"cotizacion": cotizacion})

    else:
        form = CotizacionForm()

    tipos_disponibles = TipoBodega.objects.all()
    bodegas_seleccionadas = Bodega.objects.filter(disponible=True)
    return render(
        request,
        "cotizacion/cotizar.html",
        {"form": form, "tipos_disponibles": tipos_disponibles, "bodegas_seleccionadas": bodegas_seleccionadas},
    )

@login_required
def cotizacion(request):
    try:
            cotizacion = Cotizacion.objects.get(usuario=request.user)
    except Cotizacion.DoesNotExist:
        return redirect('cotizacion:cotizar')

        cotizacion.calcular_total()

        bodegas = cotizacion.bodegas.all()

        context = {
            'bodegas': bodegas,
            'precio_total': cotizacion.precio_total,
        }
        return render(request, 'cotizacion/cotizacion.html', context)
