from django.shortcuts import render
from rest_framework.generics import DestroyAPIView
from medico.models import MedicoM
from medico.serializers import MedicoSerializer
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import RetrieveUpdateAPIView



class EliminarMedico(DestroyAPIView):
    queryset = MedicoM.objects.all()
    serializer_class = MedicoSerializer
    lookup_field = 'pk'

class ActualizarMedico(RetrieveUpdateAPIView):
    queryset = MedicoM.objects.all()
    serializer_class = MedicoSerializer
    lookup_field = 'pk'
