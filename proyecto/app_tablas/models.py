from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=80)
    email = models.EmailField()
    tfno = models.CharField(max_length=9)

    def __str__(self):
        return (self.nombre)

class Articulo(models.Model):
    nombre = models.CharField(max_length=50)
    seccion = models.CharField(max_length=20)
    precio = models.IntegerField()

    def __str__(self):
        return (self.nombre)


class Pedido(models.Model):
    numero = models.IntegerField()
    fecha = models.DateField()
    entregado = models.BooleanField()
    
    def __str__(self):
        return (self.nombre)


