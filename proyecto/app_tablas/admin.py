from django.contrib import admin

# Register your models here.

from .models import Cliente, Articulo, Pedido

admin.site.register(Cliente)
admin.site.register(Articulo)
admin.site.register(Pedido)
