from rest_framework import serializers
from .models import MedicoM
from .models import opciones_especialidades
from .models import ciudades


class MedicoSerializer(serializers.ModelSerializer):
    Especialidad = serializers.ChoiceField(choices=opciones_especialidades)
    CiudadMed = serializers.ChoiceField(choices=ciudades)
    class Meta:
        model = MedicoM
        fields = ('IdMedico', 'NombreCompletoMed', 'TelefonoMed','NumeroTarjetaMed','CedulaMed','CorreoMed', 'CiudadMed', 'Especialidad', 'DireccionConsultorio','HoraInicio', 'HoraFinal', 'FechasDisponibilidad', 'PerfilProfesional', 'Activo')