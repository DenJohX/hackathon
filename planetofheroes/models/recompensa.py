from django.db import models
from .campania import Campania


class Recompensa(models.Model):
    #id = models.IntegerField(primary_key=True)
    descripcion = models.TextField(blank=True)
    monto = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    class Meta:
        app_label = 'planetofheroes'
