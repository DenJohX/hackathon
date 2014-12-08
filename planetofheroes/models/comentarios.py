from django.db import models
from .campania import Campania


class Comentarios(models.Model):
    #id = models.IntegerField(primary_key=True)
    campania = models.ForeignKey(Campania)
    tipo = models.TextField(blank=True)
    comentario = models.TextField(blank=True)

    class Meta:
        app_label = 'planetofheroes'