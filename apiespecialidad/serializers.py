from rest_framework import serializers
from .models import Especialidad
<<<<<<< HEAD
from .models import opciones_especialidades
=======
import json
>>>>>>> 739df87cc2caddf09db554ecb99d4d94c314ac5e

# Create your models here.

with open('models/ciupac.json', 'r') as f:
    ciudad = json.load(f)

opciones_ciudades = ciudad['opciones_ciudades']

class EspecialidadSerializer(serializers.ModelSerializer):
    especialidad = serializers.ChoiceField(choices=opciones_especialidades)
    class Meta:
        model = Especialidad
        fields = ('codEspecialidad', 'especialidad')