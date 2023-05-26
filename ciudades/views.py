from django.shortcuts import render

# Create your views here.

from django.shortcuts import HttpResponse
from ciudades.models import Ciudad
import json

def cargar_datos_desde_json(request):
    with open('ciudades/ciudad.json', encoding='utf-8') as file:
        data = json.load(file)

    for item in data:
        id = item['id']
        city = item['city']
        ciudad = Ciudad(id=id, city=city)
        ciudad.save()

    return HttpResponse("Datos cargados exitosamente desde el archivo JSON.")
