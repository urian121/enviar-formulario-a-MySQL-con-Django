from django.db import models


class Empleado(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    edad = models.IntegerField(max_length=2)
