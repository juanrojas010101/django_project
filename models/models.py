from django.db import models

# Create your models here.
class Medico(models.Model):
    idMedico = models.IntegerField(primary_key=True)
    cedulaMed = models.IntegerField()
    nombreMed = models.CharField(max_length=35)
    apellidoMed = models.CharField(max_length=35)
    telefonoMed = models.CharField(max_length=10)
    correoMed = models.EmailField()
    hojaDeVidaMed = models.BinaryField()
    codEspecialidadM = models.IntegerField()

