from django.db import models

import json

# Create your models here.

with open('apipaciente/ciudades.json', 'r') as f:
    ciudad = json.load(f)

opciones_ciudades = ciudad['opciones_ciudades']


class Paciente(models.Model):
    idPaciente = models.IntegerField(primary_key=True)
    NombreCompletoPac = models.CharField(max_length=80)
    FechaNacimientoPac = models.DateField()
    cedulaPac = models.IntegerField()
    telefonoPac = models.CharField(max_length=10)
    correoPac = models.EmailField()
    direccionPac = models.CharField(max_length=40)
    ciudad = models.CharField(max_length=50, choices=opciones_ciudades)





