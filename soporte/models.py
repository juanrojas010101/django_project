from django.db import models


# Create your models here.
class Soporte(models.Model):
    Nombre = models.CharField(max_length=100)
    Apellido = models.CharField(max_length=100)
    Correo = models.EmailField()
    Mensaje = models.TextField()