from django.db import models
from django.contrib.auth.models import User


class TipoBodega(models.Model):
    """
    Representa un tipo de bodega en el sistema.

    Atributos:
        tipo (str): Nombre único del tipo de bodega.
        metros_cuadrados (int): Tamaño en metros cuadrados de la bodega.
        preparada_quimicos (bool): Indica si está preparada para químicos industriales.
        preparada_organicos (bool): Indica si está preparada para materiales orgánicos.
        hermetica (bool): Indica si la bodega es hermética.
        precio_mensual (int): Precio mensual de la bodega en pesos.
    """

    tipo = models.CharField(max_length=255, unique=True)
    metros_cuadrados = models.PositiveIntegerField()
    preparada_quimicos = models.BooleanField(default=False)
    preparada_organicos = models.BooleanField(default=False)
    hermetica = models.BooleanField(default=False)
    precio_mensual = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.tipo} ({self.metros_cuadrados} m²) - ${self.precio_mensual}/mes"


class Bodega(models.Model):
    """
    Representa una bodega específica en el sistema.

    Atributos:
        codigo (str): Código único que identifica la bodega.
        tipo_bodega (TipoBodega): Relación con el tipo de bodega.
        disponible (bool): Indica si la bodega está disponible para ser alquilada.
    """

    codigo = models.CharField(max_length=10, unique=True)
    tipo_bodega = models.ForeignKey(
        TipoBodega, on_delete=models.CASCADE, related_name="bodegas"
    )
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return f"Bodega {self.codigo} - {self.tipo_bodega.tipo}"


class Cotizacion(models.Model):
    """
    Representa una cotización de bodegas realizada por un usuario.

    Atributos:
        user (User): Usuario que realizó la cotización.
        bodegas (QuerySet[Bodega]): Conjunto de bodegas incluidas en la cotización.
        precio_total (int): Precio total calculado de las bodegas seleccionadas.

    Métodos:
        calcular_precio_total(): Calcula la suma del precio mensual de las bodegas seleccionadas.
    """

    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    bodegas = models.ManyToManyField(Bodega, related_name="cotizaciones")
    precio_total = models.PositiveIntegerField(default=0)

    def calcular_total(self):
        """Calcula el precio total de las bodegas seleccionadas."""
        self.precio_total = sum(
            bodega.tipo_bodega.precio_mensual for bodega in self.bodegas.all()
        )
        self.save()
    #RECORDATORIO: llamar al método calcular_total usando cotizacion.calcular_total antes de llamar al método save() en lugares donde se modifica la cotización (al agregar o eliminar bodegas, en vistas o formularios)