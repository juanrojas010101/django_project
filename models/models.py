from django.db import models

# Create your models here.
class Medico(models.Model):
    idMedico = models.IntegerField(primary_key=True)
    NombreCompletoMed = models.CharField(max_length=80)
    NumeroTarjetaMed = models.CharField(max_length=50)
    cedulaMed = models.IntegerField()
    telefonoMed = models.CharField(max_length=10)
    correoMed = models.EmailField()


