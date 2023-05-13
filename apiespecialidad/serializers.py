from rest_framework import serializers
from .models import Especialidad
import json

# Create your models here.

with open('models/ciupac.json', 'r') as f:
    ciudad = json.load(f)

opciones_ciudades = ciudad['opciones_ciudades']

class EspecialidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Especialidad
        fields = ('codEspecialidad', 'especialidad')