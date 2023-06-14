from django.db import models

# Create your models here.

class Agendar(models.Model):
    IdEspecialista = models.IntegerField(null=True)
    IdMedico = models.IntegerField(null=True)
    Fecha = models.DateField()
    Motivo = models.TextField()
    Hora = models.TimeField()
    Tipodeconsulta = models.CharField(max_length=80)

