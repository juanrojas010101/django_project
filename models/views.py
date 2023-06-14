from django.shortcuts import render
from rest_framework.generics import DestroyAPIView
from models.models import Medico
from models.serializers import MedicoSerializer
from rest_framework.generics import DestroyAPIView


from rest_framework.generics import RetrieveUpdateAPIView



class EliminarMedico(DestroyAPIView):
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer
    lookup_field = 'pk'

class ActualizarMedico(RetrieveUpdateAPIView):
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer
    lookup_field = 'pk'


# def consulta_medicos(request):
#      # Consulta con una condición WHERE
#      nombre_medico = request.GET.get('NombreCompletoMed')
#      numero_tarjeta = request.GET.get('NumeroTarjetaMed')

#      # Realizar la consulta con las condiciones WHERE utilizando Q
#      queryset = Medico.objects.filter(
#          Q(NombreCompletoMed=nombre_medico) | Q(NumeroTarjetaMed=numero_tarjeta)
#      )
#      resultados = [
#          {
#              'idMedico': medico.idMedico,
#              'NombreCompletoMed': medico.NombreCompletoMed,
#              'NumeroTarjetaMed' : medico.NumeroTarjetaMed
#              # Agrega otros campos según tus necesidades
#          }
#          for medico in queryset
#      ]

#      return JsonResponse(resultados, safe=False)

# from models.models import Medico
# from django.db.models import Q
# from django.http import JsonResponse

# def consulta_medicos(request):
#     id_especialista = request.GET.get('IdEspecialista')
#     id_medico = request.GET.get('IdMedico')
#     nombre_medico = request.GET.get('NombreCompletoMed')
#     numero_tarjeta = request.GET.get('NumeroTarjetaMed')

#     queryset = Medico.objects.all()

#     if id_especialista:
#         queryset = queryset.filter(IdEspecialista=id_especialista)

#     if id_medico:
#         queryset = queryset.filter(IdMedico=id_medico)

#     queryset = queryset.filter(
#         Q(NombreCompletoMed=nombre_medico) | Q(NumeroTarjetaMed=numero_tarjeta)
#     )

#     resultados = [
#         {
#             'idMedico': medico.idMedico,
#             'NombreCompletoMed': medico.NombreCompletoMed,
#             'NumeroTarjetaMed': medico.NumeroTarjetaMed
#             # Agrega otros campos según tus necesidades
#         }
#         for medico in queryset
#     ]

#     return JsonResponse(resultados, safe=False)


