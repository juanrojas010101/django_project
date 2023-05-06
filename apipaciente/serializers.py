from rest_framework import serializers
from .models import Paciente
from rest_framework import serializers
from rest_framework import serializers
from 


class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = ('idPaciente', 'cedulaPac', 'NombreCompletoPac', 'telefonoPac', 'correoPac', 'direccionPac', 'FechaNacimientoPac', 'cuidadPac')
        