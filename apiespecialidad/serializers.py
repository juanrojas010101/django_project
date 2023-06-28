from rest_framework import serializers
from .models import Especialidad
from .models import opciones_especialidades


class EspecialidadSerializer(serializers.ModelSerializer):
    especialidad = serializers.ChoiceField(choices=opciones_especialidades)
    class Meta:
        model = Especialidad
        fields = ('codEspecialidad', 'especialidad', 'guidEspecialista')