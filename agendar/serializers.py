from rest_framework import serializers
from .models import Agendar



class AgendarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agendar
        fields = ('Fecha', 'Motivo', 'Hora', 'Tipodeconsulta', 'IdEspecialista','IdMedico')