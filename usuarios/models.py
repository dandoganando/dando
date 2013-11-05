from django.db import models
from django.contrib.auth.models import User
from tiendas.models import Productos

# Create your models here.
class Usuario(models.Model):
    usuario = models.OneToOneField(User)
    fecha_nac = models.DateField()
    numero = models.IntegerField(max_length=25)
    nacionalidad = models.CharField(max_length=20)


class Direccion_Usuario(models.Model):
	user = models.ForeignKey(User)
	direccion = models.CharField(max_length=250)
	estatus = models.CharField(max_length=10)

class Tarjeta_Usuario(models.Model):
	user = models.ForeignKey(User)
	tarjeta = models.IntegerField(max_length=16)
	nombre_tarjeta = models.CharField(max_length=200)
	mes_expiracion = models.IntegerField(max_length=2)
	anio_expiracion = models.IntegerField(max_length=4)
	codigo_seguridad = models.IntegerField(max_length=3)
	metodo_pago = models.CharField(max_length=10)
	status = models.CharField(max_length=10)

class Ordenes(models.Model):
	user = models.ForeignKey(User)
	producto = models.ForeignKey(Productos)
	unidades = models.IntegerField(max_length=5)
	valor_total = models.DecimalField(max_digits=10, decimal_places=2)
	fec_emision = models.DateTimeField(auto_now=True)
	status = models.CharField(max_length=10)
	tracking = models.BigIntegerField()
	fec_envio = models.DateTimeField()
	direccion = models.ForeignKey('Direccion_Usuario')
	tarjeta = models.ForeignKey('Tarjeta_Usuario')

class Shipping(models.Model):
	nombre = models.CharField(max_length=50)
	descripcion = models.CharField(max_length=200)
	observaciones = models.TextField()

class Carrito(models.Model):
	usuario = models.ForeignKey(User)
	producto = models.ForeignKey(Productos)
	unidades = models.IntegerField(max_length=5)
	fec_ult_mod = models.DateTimeField()
	shipping = models.ForeignKey('Shipping')

class Wish_List(models.Model):
	usuario = models.ForeignKey(User)
	producto = models.ForeignKey(Productos)
	fec_agregado = models.DateTimeField(auto_now=True)