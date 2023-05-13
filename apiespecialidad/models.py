from django.db import models

# Create your models here.

class Especialidad(models.Model):
    codEspecialidad = models.BigIntegerField(primary_key=True)
    especialidad = models.CharField(max_length=80,  choices=opciones_especialidades)

