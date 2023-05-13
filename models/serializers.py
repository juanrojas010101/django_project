from rest_framework import serializers
from .models import Medico
from .models import opciones_ciudades



class MedicoSerializer(serializers.ModelSerializer):
    ciudad = serializers.ChoiceField(choices=opciones_ciudades)
    class Meta:
        model = Medico
        fields = ('idMedico', 'cedulaMed', 'NombreCompletoMed', 'telefonoMed', 'correoMed', 'NumeroTarjetaMed', 'ciudad')


        
