import json
from django.core.management.base import BaseCommand, CommandError
from apipaciente.models import Ciudad

class Command(BaseCommand):
    help = 'Carga las ciudades de Colombia desde un archivo JSON'

    def add_arguments(self, parser):
        parser.add_argument('ciudades.json', type=str, help='El archivo JSON con las ciudades de Colombia')

    def handle(self, *args, **options):
        with open(options['archivo'], 'r') as f:
            ciudades = json.load(f)
        for ciudad in ciudades:
            Ciudad.objects.create(nombre=ciudad['nombre'])