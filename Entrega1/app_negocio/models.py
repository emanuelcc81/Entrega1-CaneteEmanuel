from django.db import models

# Create your models here.
class Productos(models.Model):
    nombre = models.CharField(max_length=40)
    precio = models.FloatField()

class Datos_productos(models.Model):
    nombre = models.CharField(max_length=40)
    marca = models.CharField(max_length=40)
    fecha_fab = models.DateField()

class Proveedores(models.Model):
    nombre = models.CharField(max_length=40)
    telefono = models.IntegerField()
    