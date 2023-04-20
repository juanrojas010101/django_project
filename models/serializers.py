from rest_framework import serializers
from .models import Medico
from .models import Especialidad
from .models import Servicio

class MedicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medico
        fields = ('idMedico', 'cedulaMed', 'nombreMed', 'apellidoMed', 'telefonoMed', 'correoMed', 'hojaDeVidaMed')
        read_only_fields= ('codEspecialidadM', )
        
class EspecialidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Especialidad 
        fields = ('codEspecialidad','especialidad') 
        

class ServicioSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Servicio
        fields = ('codigoCita', 'fechaCM', 'horaCM', 'descripcionCM', 'codTipoCitaC', 'idPacienteC', 'idMedicoC')
    
class TipoServicioSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Especialidad 
        fields = ('codTipoCita', 'tipoCita')