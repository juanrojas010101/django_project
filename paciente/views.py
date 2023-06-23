from django.shortcuts import render
from rest_framework.generics import DestroyAPIView
from paciente.models import PacienteM
from paciente.serializers import PacienteSerializer
from rest_framework.generics import RetrieveUpdateAPIView


class EliminarPaciente(DestroyAPIView):
    queryset = PacienteM.objects.all()
    serializer_class = PacienteSerializer
    lookup_field = 'pk'

class ActualizarPaciente(RetrieveUpdateAPIView):
    queryset = PacienteM.objects.all()
    serializer_class = PacienteSerializer
    lookup_field = 'pk'

