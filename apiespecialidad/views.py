from django.shortcuts import render

from rest_framework.generics import DestroyAPIView
from apiespecialidad.models import Especialidad
from apiespecialidad.serializers import EspecialidadSerializer
from rest_framework.generics import RetrieveUpdateAPIView

class EliminarEspecialidad(DestroyAPIView):
    queryset = Especialidad.objects.all()
    serializer_class = EspecialidadSerializer
    lookup_field = 'pk'
    
class ActualizarEspecialidad(RetrieveUpdateAPIView):
    queryset = Especialidad.objects.all()
    serializer_class = EspecialidadSerializer
    lookup_field = 'pk'
    