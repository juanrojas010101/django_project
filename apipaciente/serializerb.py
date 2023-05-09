import json
from rest_framework import serializers
from .models import Paciente
from rest_framework import serializers
from rest_framework import serializers


##class CiudadSerializer(serializers.Field):
    ##def to_representation(self, value):
        ##with open('ciudades.json', 'r') as f:
            ##ciudad = json.load(f)
        ##ciudad = next((c for c in ciudad if c['ciudades'] == value), None)
        ##return ciudad

    ##def to_internal_value(self, data):
        ##return data
class CiudadSerializer(serializers.Serializer):
    ciudad = serializers.JSONField()

    def create(self, validated_data):
        return validated_data

    def update(self, instance, validated_data):
        instance.update(validated_data)
        return instance

    def to_representation(self, instance):
        data = super().to_representation(instance)
        ciudad = [
            {"name": "Guayabal de Síquima"},
            {"name": "Puerto Escondido"},
            {"name": "El Cerrito"},
            {"name": "Planadas"},
            {"name": "Tunja"},
            {"name": "San Francisco"},
            {"name": "Corinto"},
            {"name": "Algeciras"},
            {"name": "La Victoria"},
            {"name": "San Juan Nepomuceno"},
            {"name": "El Paujil"},
            {"name": "Salamina"},
            {"name": "San Andrés de Cuerquía"},
            {"name": "Samaniego"},
            {"name": "Tolú"},
            {"name": "La Jagua del Pilar"},
            {"name": "San Juan de Arama"},
            {"name": "Valdivia"},
            {"name": "San José del Palmar"},
            {"name": "San Juan de Rioseco"},
            {"name": "La Vega"},
            {"name": "Yacuanquer"},
            {"name": "San Luis"},
            {"name": "Ansermanuevo"},
            {"name": "El Tablón de Gómez"},
            {"name": "Lebrija"},
            {"name": "Páez"},
            {"name": "Luruaco"},
            {"name": "Sonsón"},
            {"name": "Támesis"},
            {"name": "Buenavista"},
            {"name": "San Sebastián"},
            {"name": "Guachucal"},
            {"name": "Piamonte"},
            {"name": "San Vicente del Caguán"},
            {"name": "Marmato"},
            {"name": "San José de Miranda"},
            {"name": "Purísima"},
            {"name": "La Belleza"},
            {"name": "Santuario"},
            {"name": "Gambita"},
            {"name": "San Pablo de Borbur"},
            {"name": "San Carlos"},
            {"name": "Cantagallo"},
            {"name": "Tello"},
            {"name": "Oporapa"},
            {"name": "Silvia"},
            {"name": "Santa Rosa de Cabal"},
            {"name": "La Apartada y La Frontera"},
            {"name": "Valparaíso"},
            {"name": "Santiago"},
            {"name": "Pijao"},
            {"name": "Candelaria"},
            {"name": "Supía"},
            {"name": "La Playa de Belén"},
            {"name": "San Carlos"},
            {"name": "La Montañita"},
            {"name": "El Retorno"},
            {"name": "Pulí"},
            {"name": "Vélez"}
        ]
        data["ciudades"] = ciudad
        return data