from django.shortcuts import render

from rest_framework.generics import DestroyAPIView
from apiespecialidad.models import Especialidad
from apiespecialidad.serializers import EspecialidadSerializer

class EliminarEspecialidad(DestroyAPIView):
    queryset = Especialidad.objects.all()
    serializer_class = EspecialidadSerializer
    lookup_field = 'pk'
    
    
    