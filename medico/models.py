from django.db import models



class MedicoM(models.Model):
    IdMedico = models.AutoField(primary_key=True)
    NombreCompletoMed = models.CharField(max_length=80)
    NumeroTarjetaMed = models.CharField(max_length=50)
    CedulaMed = models.IntegerField(null=True)
    CorreoMed = models.EmailField(null=True)
    TelefonoMed = models.CharField(max_length=10)
    CiudadMed = models.CharField(max_length=90)
    Especialidad = models.CharField(max_length=50)
    DireccionConsultorio = models.CharField(max_length=50, null=True, blank=True)
    HoraInicio = models.CharField(max_length=1000, null=True, blank=True)
    HoraFinal = models.CharField(max_length=1000, null=True, blank=True)
    FechasDisponibilidad = models.CharField(max_length=1000, null=True, blank=True)
    PerfilProfesional = models.CharField(max_length=500, null=True, blank=True)
    Activo = models.BooleanField(null=True, blank=True)


