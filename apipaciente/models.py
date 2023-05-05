from django.db import models

# Create your models here.

class Paciente(models.Model):
    idPaciente = models.IntegerField(primary_key=True)
    NombreCompletoPac = models.CharField(max_length=90)
    FechaNacimientoPac = models.DateField()
    cedulaPac = models.IntegerField()
    telefonoPac = models.CharField(max_length=10)
    correoPac = models.EmailField()
    direccionPac = models.CharField(max_length=30)

   