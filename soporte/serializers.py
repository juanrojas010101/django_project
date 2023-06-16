from rest_framework import serializers
from .models import Soporte

class SoporteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Soporte
        fields = ('Nombre', 'Apellido', 'Correo', 'Mensaje')
