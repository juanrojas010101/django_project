from rest_framework import serializers
from .models import Medico





class MedicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medico
        fields = ('idMedico', 'NombreCompletoMed', 'telefonoMed','NumeroTarjetaMed','cedulaMed','correoMed', 'ciudadMed', 'especialidad', 'direccionConsultorio', 'IdEspecialidad', 'IdCiudad','HoraInicio', 'HoraFinal', 'FechasDisponibilidad', 'PerfilProfesional', 'Activo')



        
