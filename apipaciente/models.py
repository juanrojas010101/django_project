from django.db import models

# Create your models here.

class Paciente(models.Model):
    idPaciente = models.IntegerField(primary_key=True)
    cedulaPac = models.IntegerField()
    nombrePac = models.CharField(max_length=15)
    apellidoPac =  models.CharField(max_length=15)
    edadPac = models.IntegerField()
    telefonoPac = models.CharField(max_length=10)
    correoPac = models.EmailField()
    direccionPac = models.CharField(max_length=30)

   