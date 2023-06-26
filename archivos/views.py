from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from archivos.models import Archivo
from archivos.serializers import ArchivoSerializer

class ArchivoView(APIView):
    def get(self, request):
        # Lógica para obtener la lista de archivos
        archivos = Archivo.objects.all()
        # Serializa los archivos para representarlos en formato JSON
        serializer = ArchivoSerializer(archivos, many=True)
        return Response(serializer.data)

    def post(self, request):
        # Crea una instancia del modelo Archivo y guarda el archivo enviado en la solicitud
        archivo = Archivo(archivo=request.FILES['archivo'])
        archivo.save()
        return Response({'status': 'Archivo guardado correctamente'})
