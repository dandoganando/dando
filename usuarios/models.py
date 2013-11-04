from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Usuarios(models.Model):
    user = models.ForeignKey(User, unique=True)
    fecha_nac = models.DateField()
    numero = models.IntegerField(max_length=25)
    nacionalidad = models.CharField(max_length=20)

class Direccion_Usuario(models.Model):
	user = models.ForeignKey(User)
	direccion = models.CharField(max_length=250)
	estatus = models.CharField(max_length=10)
	