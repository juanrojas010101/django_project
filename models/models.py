from django.db import models


class Medico(models.Model):
    idMedico = models.AutoField(primary_key=True)
    NombreCompletoMed = models.CharField(max_length=90)
    NumeroTarjetaMed = models.CharField(max_length=30)
    cedulaMed = models.IntegerField(null=True)
    telefonoMed = models.CharField(max_length=10)
    correoMed = models.EmailField(null=True)
    ciudadMed = models.CharField(max_length=90)
    especialidad = models.CharField(max_length=50)
    direccionConsultorio = models.CharField(max_length=50)
    IdEspecialidad = models.CharField(max_length=80)
    IdCiudad = models.CharField(max_length=90)

