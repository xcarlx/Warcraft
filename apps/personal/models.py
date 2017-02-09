# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Persona(models.Model):
	usuario = models.OneToOneField(User, on_delete=models.CASCADE)
	fnacimiento = models.DateField(blank=True, null=True)
	facebook = models.CharField(max_length=100, blank=True, null=True)
	foto = models.ImageField(upload_to='personal/', blank=True, null=True)
	nikename = models.CharField(max_length=20, blank=True, null=True)
	estado = models.BooleanField(default=True)