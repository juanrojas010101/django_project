from rest_framework import serializers
from .models import Medico
from .models import Especialidad


class MedicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medico
        fields = ('idMedico', 'cedulaMed', 'nombreMed', 'apellidoMed', 'telefonoMed', 'correoMed', 'hojaDeVidaMed')
        read_only_fields= ('codEspecialidadM', )


        
class EspecialidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Especialidad 
        fields = ('codEspecialidad','especialidad') 
        