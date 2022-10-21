from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

# Create your models here.


class Noticias(models.Model):
    Titulo = models.CharField(max_length=100)
    Descripcion = models.TextField(max_length=500)
    Fecha = models.DateTimeField(auto_now_add=True)
    Autor = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,)

    def __str__(self) -> str:
        return self.Titulo

    def get_absolute_url(self):
        return reverse("noticias_detalle", args=[str(self.id)])


class Comentarios(models.Model):
    noticia = models.ForeignKey(
        Noticias,
        on_delete=models.CASCADE,
        related_name='comentarios',)
    comentario = models.CharField(max_length=200)
    autor = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,)

    def __str__(self) -> str:
        return self.comentario

    def get_absolute_url(self):
        return reverse("noticias_detalle", args=[str(self.noticia_id)])
