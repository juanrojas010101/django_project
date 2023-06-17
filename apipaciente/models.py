from django.db import models


class Paciente(models.Model):
    idPaciente = models.AutoField(primary_key=True)
    NombreCompletoPac = models.CharField(max_length=90)
    FechaNacimientoPac = models.DateField()
    cedulaPac = models.IntegerField()
    telefonoPac = models.CharField(max_length=10)
    correoPac = models.EmailField()
    ciudadPac = models.CharField(max_length=90)



