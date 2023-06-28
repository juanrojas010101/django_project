from rest_framework import serializers
from .models import Agendar



class AgendarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agendar
        fields = ('IdCita','Fecha', 'Motivo', 'Hora', 'Tipodeconsulta', 'IdEspecialista','IdMedico', 'Estados', 'IdPaciente')