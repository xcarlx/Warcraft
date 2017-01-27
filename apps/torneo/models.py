from __future__ import unicode_literals

from django.db import models
from ..personal.models import Persona

# Create your models here.

class Juego(models.Model):
	nombre = models.CharField(max_length=50)
	orden = models.IntegerField()


class Jugador(models.Model):
	nick = models.CharField(max_length=30)
	persona = models.ForeignKey(Persona)
	estado = models.BooleanField(default=True)

