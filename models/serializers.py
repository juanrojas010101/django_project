from rest_framework import serializers
from .models import Medico
<<<<<<< HEAD
from .models import opciones_ciupac
=======
from .models import opciones_ciudades
>>>>>>> 739df87cc2caddf09db554ecb99d4d94c314ac5e



class MedicoSerializer(serializers.ModelSerializer):
<<<<<<< HEAD
    ciudadMed = serializers.ChoiceField(choices=opciones_ciupac)
    class Meta:
        model = Medico
        fields = ('idMedico', 'cedulaMed', 'NombreCompletoMed', 'telefonoMed', 'correoMed', 'NumeroTarjetaMed','ciudadMed')
=======
    ciudad = serializers.ChoiceField(choices=opciones_ciudades)
    class Meta:
        model = Medico
        fields = ('idMedico', 'cedulaMed', 'NombreCompletoMed', 'telefonoMed', 'correoMed', 'NumeroTarjetaMed', 'ciudad')
>>>>>>> 739df87cc2caddf09db554ecb99d4d94c314ac5e


        
