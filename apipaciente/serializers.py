from rest_framework import serializers
from .models import Paciente


class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = ('idPaciente', 'cedulaPac', 'nombrePac', 'apellidoPac', 'telefonoPac', 'correoPac', 'direccionPac', 'edadPac')