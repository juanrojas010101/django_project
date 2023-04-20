from .models import Medico
from .models import Servicio
from rest_framework import viewsets, permissions
from .serializers import MedicoSerializer
from .serializers import EspecialidadSerializer
from .serializers import ServicioSerializer
from .serializers import TipoServicioSerializer

class ModelsViewSet(viewsets.ModelViewSet):
    queryset = Medico.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = MedicoSerializer
    def get_serializer_class(self):
        if self.action == 'list':
            return EspecialidadSerializer
        else:
            return MedicoSerializer 

class ServicioViewSet(viewsets.ModelViewSet):
    queryset = Servicio.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ServicioSerializer
    def get_serializer_class(self):
        if self.action == 'list':
            return TipoServicioSerializer
        else:
            return ServicioSerializer 


    