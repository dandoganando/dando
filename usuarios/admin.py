from usuarios.models import Usuario, Direccion_Usuario, Tarjeta_Usuario, Ordenes, Shipping, Carrito, Wish_List
from django.contrib import admin

admin.site.register(Usuario)
admin.site.register(Direccion_Usuario)
admin.site.register(Tarjeta_Usuario)
admin.site.register(Ordenes)
admin.site.register(Shipping)
admin.site.register(Carrito)
admin.site.register(Wish_List)