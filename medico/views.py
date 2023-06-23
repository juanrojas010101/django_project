from django.shortcuts import render
from rest_framework.generics import DestroyAPIView
from medico.models import MedicoM
from medico.serializers import MedicoSerializer
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import RetrieveUpdateAPIView
from .serializers import MedicoSerializer



class EliminarMedico(DestroyAPIView):
    queryset = MedicoM.objects.all()
    serializer_class = MedicoSerializer
    lookup_field = 'pk'

class ActualizarMedico(RetrieveUpdateAPIView):
    queryset = MedicoM.objects.all()
    serializer_class = MedicoSerializer
    lookup_field = 'pk'

# from rest_framework.response import Response
# from rest_framework.views import APIView
# import json
# from .models import ciudades

# Abre el archivo JSON y carga los datos
# with open('medico/ciudad.json', encoding='utf-8') as file:
#     data = json.load(file)

# # Extrae los nombres de las ciudades en una lista
# ciudades = [item['city'] for item in data]


# class CiudadView(APIView):
#     def post(self, request):
#         serializer = MedicoSerializer(data={'CiudadMed': ciudades})
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
