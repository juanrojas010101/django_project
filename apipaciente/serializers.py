from rest_framework import serializers
from .models import Paciente
from rest_framework import serializers
from rest_framework import serializers
from .models import opciones_ciudades



class PacienteSerializer(serializers.ModelSerializer):
    ciudadPac = serializers.ChoiceField(choices=opciones_ciudades)
    class Meta:
        model = Paciente
        fields = ('idPaciente', 'cedulaPac', 'NombreCompletoPac', 'telefonoPac', 'correoPac', 'direccionPac', 'FechaNacimientoPac', 'ciudadPac')



        