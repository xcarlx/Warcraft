# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ..personal.models import Persona as Jugador

# Create your models here.

class Juego(models.Model):
	nombre = models.CharField(max_length=50)
	categoria = models.CharField(max_length=50)
	estado = models.BooleanField(default=True)


class PerfilJuego(models.Model):
	ALEATORIO = "ALE"
	ORCO = "ORC"
	HUMANO = "HUM"
	ELFO = "ELF"
	RAZA = ((ALEATORIO, 'Aleatorio'), (ORCO, 'Orco'), (HUMANO, 'Humano'), (ELFO, 'Elfo nocturno'))
	jugador = models.ForeignKey(Jugador)
	juego = models.ForeignKey(Juego)
	raza = models.CharField(max_length=20, choices=RAZA, default=ALEATORIO)


class Toreno(models.Model):
	nombre = models.CharField(max_length=50)
	descripcion = models.CharField(max_length=250)
	estado = models.BooleanField(default=True)


class Inscripcion(models.Model):
	torneo = models.ForeignKey(Toreno)
	jugador = models.ForeignKey(Jugador)
	estado = models.BooleanField(default=True)


class ConfigInscrito(models.Model):
	orden = models.IntegerField()
	codigo = models.CharField(max_length=5)
	cantidad = models.IntegerField()
	cant_rondas = models.IntegerField()

class Ronda(models.Model):
	orden = models.IntegerField()
	nombre = models.CharField(max_length=50)
	cantidad = models.IntegerField()
	config_inscrito = models.ForeignKey(ConfigInscrito)

class ConfigTorneo(models.Model):
	torneo = models.ForeignKey(Toreno)
	juego = models.ForeignKey(Juego)
	config_inscrito = models.ForeignKey(ConfigInscrito)
	estado = models.CharField(max_length=20)

class Mapa(models.Model):
	nombre = models.CharField(max_length=50)
	iniciales = models.CharField(max_length=2)
	descripcion = models.CharField(max_length=200)

class Versus(models.Model):
	inscrito1 = models.ForeignKey(Inscripcion, related_name='jugador1', blank=True, null=True)
	inscrito2 = models.ForeignKey(Inscripcion ,related_name='jugador2',blank=True, null=True)
	inscrito_ganador = models.ForeignKey(Inscripcion,related_name='ganador', blank=True, null=True)
	mapa = models.CharField(max_length=50,blank=True, null=True)
	replay = models.CharField(max_length=50, blank=True, null=True)
	nro_versus = models.IntegerField(blank=True, null=True)
	versus_ganador1 = models.ForeignKey("self", related_name='ganador_anterior1', blank=True, null=True)
	versus_ganador2 = models.ForeignKey("self", related_name='ganador_anterior2', blank=True, null=True)
	ronda = models.ForeignKey(Ronda, blank=True, null=True)
