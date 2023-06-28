from django.db import models
import json
import uuid


# Create your models here.


with open('apiespecialidad/especialidades.json', 'r') as f:
    especialidad = json.load(f)
opciones_especialidades = especialidad['opciones_especialidades']

class Especialidad(models.Model):
    codEspecialidad = models.BigIntegerField(primary_key=True)
    especialidad = models.CharField(max_length=35, choices=opciones_especialidades)
    guidEspecialista = models.UUIDField(default=uuid.uuid4, editable=False)


