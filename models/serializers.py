from rest_framework import serializers
from .models import Medico



class MedicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medico
        fields = ('idMedico', 'cedulaMed', 'nombreMed', 'apellidoMed', 'telefonoMed', 'correoMed', 'hojaDeVidaMed','codEspecialidadM')


        
