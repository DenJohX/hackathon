from django.db import models
from django.contrib.auth.models import User
from .campania import Campania


class Donacion(models.Model):
    #id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(User, related_name='rel_donacion')
    campania = models.ForeignKey(Campania)
    monto = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    comentario = models.TextField(blank=True)
    recompensa = models.IntegerField(blank=True, null=True)

    class Meta:
        app_label = 'planetofheroes'
