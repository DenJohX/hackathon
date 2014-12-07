from django.db import models

class Campania(models.Model):
    #id = models.IntegerField(primary_key=True)
    tipo = models.TextField(blank=True)
    monto = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    titulo = models.TextField(blank=True)
    direccion = models.TextField()
    foto = models.ImageField()
    categoria = models.CharField(max_length=80, blank=True)
    historia = models.TextField()
    inicia = models.DateTimeField(blank=True, null=True)
    recaudado = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    voluntarios = models.IntegerField(blank=True, null=True)
