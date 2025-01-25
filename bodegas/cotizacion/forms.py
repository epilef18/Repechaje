from django import forms
from .models import Bodega

class CotizacionForm(forms.Form):
    tipo_bodega = forms.ModelChoiceField(
        queryset=Bodega.objects.filter(disponible=True).select_related('tipo_bodega'),
        empty_label="Elija un tipo de bodega",
        label="Seleccione tipo de Bodega",
    )