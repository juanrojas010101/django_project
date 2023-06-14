from django.db import models

# Create your models here.

class Agendar(models.Model):
    IdEspecialista = models.CharField(max_length=90)
    IdMedico = models.CharField(max_length=90)
    Fecha = models.DateField()
    Motivo = models.TextField()
    Hora = models.TimeField()
    Tipodeconsulta = models.CharField(max_length=80)

