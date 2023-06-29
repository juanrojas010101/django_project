from rest_framework import serializers
from .models import MedicoM


class MedicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicoM
        fields = ('IdMedico', 'NombreCompletoMed', 'TelefonoMed','NumeroTarjetaMed','CedulaMed','CorreoMed', 'CiudadMed', 'Especialidad', 'DireccionConsultorio','HoraInicio', 'HoraFinal', 'FechasDisponibilidad', 'PerfilProfesional', 'Activo', 'guidEspecialista', 'fotoPerfil')