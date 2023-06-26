from rest_framework import serializers
from .models import Archivo

class ArchivoSerializer(serializers.ModelSerializer):
    archivo = serializers.FileField(required=False)

    class Meta:
        model = Archivo
        fields = '__all__'

