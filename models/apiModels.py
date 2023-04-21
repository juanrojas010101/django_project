from .models import Medico
from rest_framework import viewsets, permissions
from .serializers import MedicoSerializer
from .serializers import EspecialidadSerializer


class ModelsViewSet(viewsets.ModelViewSet):
    queryset = Medico.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = MedicoSerializer
    def get_serializer_class(self):
        if self.action == 'list':
            return EspecialidadSerializer
        else:
            return MedicoSerializer 



    