from .models import Paciente
from .serializers import PacienteSerializer
from rest_framework import viewsets, permissions

        
class PacienteViewSet(viewsets.ModelViewSet):
    queryset = Paciente.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = PacienteSerializer
    
