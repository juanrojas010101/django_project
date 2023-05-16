from django.db import models
import json

# Create your models here.

with open('models/ciupac.json', 'r') as f:
    ciudadMed = json.load(f)

opciones_ciupac = ciudadMed['opciones_ciupac']
# Create your models here.
class Medico(models.Model):
    idMedico = models.IntegerField(primary_key=True)
    NombreCompletoMed = models.CharField(max_length=90)
    NumeroTarjetaMed = models.CharField(max_length=30)
    cedulaMed = models.IntegerField()
    telefonoMed = models.CharField(max_length=10)
    correoMed = models.EmailField()
    ciudadMed = models.CharField(max_length=100, choices=opciones_ciupac)


