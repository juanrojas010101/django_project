from 
import serializers 
from .models import models

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = models
        fields = ('idMedico', 'cedulaMed', 'nombreMed', 'apellidoMed', 'telefonoMed', 'correoMed', 'hojaDeVidaMed', 'codEspecialidadM')