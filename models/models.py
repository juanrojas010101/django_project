from django.db import models


class Medico(models.Model):
    idMedico = models.AutoField(primary_key=True)
    NombreCompletoMed = models.CharField(max_length=90)
    NumeroTarjetaMed = models.CharField(max_length=50)
    cedulaMed = models.IntegerField(null=True)
    correoMed = models.EmailField(null=True)
    telefonoMed = models.CharField(max_length=10)
    ciudadMed = models.CharField(max_length=90)
    especialidad = models.CharField(max_length=50)
    direccionConsultorio = models.CharField(max_length=50)
    IdEspecialidad = models.CharField(max_length=80)
    IdCiudad = models.CharField(max_length=90)
    HoraInicio = models.CharField(max_length=1000)
    HoraFinal = models.CharField(max_length=1000)
    FechasDisponibilidad = models.CharField(max_length=1000)
    PerfilProfesional = models.CharField(max_length=500)
    Activo = models.BooleanField(null=True)

