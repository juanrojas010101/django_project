from django.db import models
import json

# Create your models here.

with open('apiespecialidad/especialidades.json', 'r') as f:
    especialidades = json.load(f)

opciones_especialidades = especialidades['opciones_especialidades']



class Especialidad(models.Model):
    codEspecialidad = models.BigIntegerField(primary_key=True)
    especialidad = models.CharField(max_length=50,  choices=opciones_especialidades)

