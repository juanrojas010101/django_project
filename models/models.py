from django.db import models
import json

# Create your models here.

with open('models/ciupac.json', 'r') as f:
    ciudad = json.load(f)

opciones_ciudades = ciudad['opciones_ciudades']

class Medico(models.Model):
    idMedico = models.IntegerField(primary_key=True)
    NombreCompletoMed = models.CharField(max_length=90)
    NumeroTarjetaMed = models.CharField(max_length=30)
    cedulaMed = models.IntegerField()
    telefonoMed = models.CharField(max_length=10)
    correoMed = models.EmailField()
    ciudad = models.CharField(max_length=350, choices=opciones_ciudades)


