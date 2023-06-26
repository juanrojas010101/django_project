from .models import Archivo
from .serializers import ArchivoSerializer
from rest_framework import viewsets, permissions

        
class ArchivoViewSet(viewsets.ModelViewSet):
    queryset = Archivo.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ArchivoSerializer