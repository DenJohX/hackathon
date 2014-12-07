from django.db import models
from .campania import Campania
from django.contrib.auth.models import User

class Voluntario(models.Model):
    #id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(User, related_name='volunter')
    campania = models.ForeignKey(Campania)
    comentario = models.TextField(blank=True)
    confirmar = models.BooleanField(default=True)
