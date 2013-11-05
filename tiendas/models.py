from django.db import models
from django.contrib.auth.models import User 

#Se crea el campo tienda 
class Tienda(models.Model):
#Empenzamos por solicitar la informacion basica del usuario 
	"""Nombre del Usuario"""
	nombre = models.CharField(max_length=200)
	"""Fehca de Nacimiento"""
	fecha_apertura = models.DateTimeField(auto_now=True)
	"""Password"""
	password = models.CharField(max_length=200)
	"""Cuenta Bancaria"""
	cuenta_bancaria = models.IntegerField(max_length=25)
	"""Correo Electronico"""
	email = models.CharField(max_length=200)
	"""Telefono"""
	telefono = models.IntegerField(max_length=20)

	region = models.ForeignKey('Region')
	lugar = models.CharField(max_length=200)
	categoria = models.ForeignKey('Categoria')
	puntuacion = models.DecimalField(decimal_places=1)

	def __unicode__(self): 
		return self.nombre 
#----------------------------------------------------------------------------------------------
class Encargados(models.Model): 
#Mostramos la informacion de los encargados de las tiendas 
	"""Nombre de la tienda"""
	tienda = models.ForeignKey('Tienda')
	"""Nombre del Usuario Encargado"""
	usuario = models.ForeignKey(User)
	"""Rango en la jerarquia de la tienda"""
	permisos = models.CharField(max_length=10)

	def __unicode__(self): 
		return self.id 
#----------------------------------------------------------------------------------------------
class Region(models.Model): 
#Mostramos de donde es la tienda 
	nombre = models.CharField(max_length=200)
	descripcion = models.TextField() 
	historia = models.TextField()
	turismo = models.TextField() 
	imagenes = models.ImageField

	def __unicode__(self): 
		return self.nombre 
#----------------------------------------------------------------------------------------------
class Productos(models.Model): 
#Mostramos los productos en venta y de donde son 
	nombre = models.CharField(max_length=200)
	tienda = models.ForeignKey('Tienda')
	descripcion = models.TextField()
	precio = models.DecimalField(decimal_places=2)
	unidades = models.IntegerField(max_lenght=3)
	puntuacion = models.DecimalField(decimal_places=1)
	historia = models.TextField()
	categoria = models.ForeignKey('Categoria')
	epoca = models.ForeignKey() 
	etiqueta = models.CharField(max_length=30)

	def __unicode__(self): 
		return self.nombre 
#----------------------------------------------------------------------------------------------
class Producto_Imagenes(models.Model):
	producto = models.ForeignKey('Productos')
	url_imagen = models.ImageField()
	numero = models.IntegerField()
	tipo = models.CharField(max_length=10)

	def __unicode__(self): 
		return self.id
#----------------------------------------------------------------------------------------------
class Productos_Reviews(models.Model): 
	usuario = models.ForeignKey(User)
	producto = models.ForeignKey('Productos')
	puntuacion = models.DecimalField(decimal_places=1)
	comentario = models.CharField(max_length=200)
	fecha_publicacion = models.DateTimeField(auto_now=True)
	fecha_cambio = models.DateTimeField(auto_now=True)

	def __unicode__(self): 
		return self.id 
#----------------------------------------------------------------------------------------------
class Tienda_Reviews(models.Model): 
	usuario = models.ForeignKey(User)
	tienda = models.ForeignKey('Tienda')
	puntuacion = models.DecimalField(decimal_places=1)
	fecha_publicacion = models.DateTimeField(auto_now=True)
	fecha_cambio = models.DateTimeField(auto_now=True)

	def __unicode__(self): 
		return self.id 

class Epoca(models.Model):
	nombre = models.CharField(max_length=200)
	descripcion = models.TextField()
	historia = models.TextField()
	imagen = models.ImageField()

	def __unicode__(self): 
		return self.nombre

class Oferta(models.Model):
	producto = models.ForeignKey('Productos')
	descuentos = models.DecimalField(decimal_places=2)
	fecha_inicio = models.DateTimeField()
	fecha_final = models. DateTimeField() 

	def __unicode__(self): 
		return self.id 


	# Create your models here.
