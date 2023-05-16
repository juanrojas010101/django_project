from django.db import models
import json


# Create your models here.


with open('apiespecialidad/especialidades.json', 'r') as f:
    especialidades = json.load(f)
opciones_especialidades = especialidades['opciones_especialidades']

class Especialidad(models.Model):
    codEspecialidad = models.BigIntegerField(primary_key=True)
<<<<<<< HEAD
    especialidad = models.CharField(max_length=35, choices=opciones_especialidades)
=======
    especialidad = models.CharField(max_length=80,  choices=opciones_especialidades)

>>>>>>> 739df87cc2caddf09db554ecb99d4d94c314ac5e
