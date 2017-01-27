from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
def user_directory_path(instance, filename):
	# file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
	return 'user_{0}/{1}'.format(instance.user.id, filename)

class Persona(models.Model):
	usuario = models.OneToOneField(User, on_delete=models.CASCADE)
	fnacimiento = models.DateField(blank=True, null=True)
	facebook = models.CharField(max_length=100, blank=True, null=True)
	foto = models.ImageField(upload_to=user_directory_path, blank=True, null=True)