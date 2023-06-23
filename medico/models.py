from django.db import models
import json

with open('medico/especialidades.json', 'r') as f:
     Especialidad = json.load(f)
opciones_especialidades = Especialidad['opciones_especialidades']

# Abre el archivo JSON y carga los datos
with open('medico/ciudad.json', 'r') as file:
    CiudadMed = json.load(file)
ciudades = CiudadMed['ciudades']



class MedicoM(models.Model):
    IdMedico = models.AutoField(primary_key=True)
    NombreCompletoMed = models.CharField(max_length=80)
    NumeroTarjetaMed = models.CharField(max_length=50)
    CedulaMed = models.IntegerField(null=True)
    CorreoMed = models.EmailField(null=True)
    TelefonoMed = models.CharField(max_length=10)
    CiudadMed = models.CharField(max_length=90)
    Especialidad = models.CharField(max_length=50)
    DireccionConsultorio = models.CharField(max_length=50)
    HoraInicio = models.CharField(max_length=1000)
    HoraFinal = models.CharField(max_length=1000)
    FechasDisponibilidad = models.CharField(max_length=1000)
    PerfilProfesional = models.CharField(max_length=500)
    Activo = models.BooleanField(null=True)


