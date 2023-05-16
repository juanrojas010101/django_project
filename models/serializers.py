from rest_framework import serializers
from .models import Medico
from .models import opciones_ciupac



class MedicoSerializer(serializers.ModelSerializer):
    ciudadMed = serializers.ChoiceField(choices=opciones_ciupac)
    class Meta:
        model = Medico
        fields = ('idMedico', 'cedulaMed', 'NombreCompletoMed', 'telefonoMed', 'correoMed', 'NumeroTarjetaMed','ciudadMed')


        
