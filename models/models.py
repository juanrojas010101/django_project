from django.db import models
import json

# Create your models here.

with open('models/ciupac.json', 'r') as f:
<<<<<<< HEAD
    ciudadMed = json.load(f)

opciones_ciupac = ciudadMed['opciones_ciupac']
# Create your models here.
=======
    ciudad = json.load(f)

opciones_ciudades = ciudad['opciones_ciudades']

>>>>>>> 739df87cc2caddf09db554ecb99d4d94c314ac5e
class Medico(models.Model):
    idMedico = models.IntegerField(primary_key=True)
    NombreCompletoMed = models.CharField(max_length=90)
    NumeroTarjetaMed = models.CharField(max_length=30)
    cedulaMed = models.IntegerField()
    telefonoMed = models.CharField(max_length=10)
    correoMed = models.EmailField()
<<<<<<< HEAD
    ciudadMed = models.CharField(max_length=100, choices=opciones_ciupac)
=======
    ciudad = models.CharField(max_length=350, choices=opciones_ciudades)
>>>>>>> 739df87cc2caddf09db554ecb99d4d94c314ac5e


