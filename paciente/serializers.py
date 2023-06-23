from rest_framework import serializers
from .models import PacienteM
from rest_framework import serializers
from rest_framework import serializers




class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = PacienteM
        fields = ('IdPaciente', 'cedulaPac', 'NombreCompletoPac', 'telefonoPac', 'correoPac', 'ciudadPac', 'FechaNacimientoPac')