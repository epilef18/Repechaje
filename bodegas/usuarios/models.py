from django.db import models
from django.contrib.auth.models import User


class Noticia(models.Model):
    """
    Representa una noticia en el sistema.

    Atributos:
        titulo (str): Título de la noticia (máximo 45 caracteres).
        cuerpo (str): Contenido o descripción detallada de la noticia.
        imagen_url (str): URL opcional de una imagen relacionada con la noticia.
    """

    titulo = models.CharField(max_length=45)
    cuerpo = models.TextField()
    imagen_url = models.URLField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.titulo


class Like(models.Model):
    """
    Representa un "me gusta" asociado a una noticia por un usuario.

    Atributos:
        user (User): Usuario que dio like a la noticia.
        noticia (Noticia): Noticia que recibió el like.

    Meta:
        unique_together: Asegura que un usuario no pueda dar más de un like a la misma noticia.
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="likes")
    noticia = models.ForeignKey(Noticia, on_delete=models.CASCADE, related_name="likes")

    class Meta:
        unique_together = (
            "user",
            "noticia",
        )  # Un usuario no puede dar like a la misma noticia más de una vez.

    def __str__(self):
        return f"{self.user.username} liked {self.noticia.titulo}"
