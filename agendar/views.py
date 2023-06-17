from django.shortcuts import render

# Create your views here.
# from .models import Agendar
# from .models import ValidationError

# def agendar_cita(request):
#     if request.method == 'POST':
#         # Obtener los datos del formulario
#         id_especialista = request.POST['id_especialista']
#         id_medico = request.POST['id_medico']
#         fecha = request.POST['fecha']
#         hora = request.POST['hora']
#         motivo = request.POST['motivo']
#         tipodeconsulta = request.POST['tipodeconsulta']

#         # Crear una instancia del modelo Agendar
#         cita = Agendar(
#             IdEspecialista=id_especialista,
#             IdMedico=id_medico,
#             Fecha=fecha,
#             Hora=hora,
#             Motivo=motivo,
#             Tipodeconsulta=tipodeconsulta
#         )

#         try:
#             # Validar la cita
#             cita.full_clean()

#             # Guardar la cita
#             cita.save()
#             return render(request, 'agendado.html')
#         except ValidationError as e:
#             error_message = str(e)
#             return render(request, 'agendar.html', {'error_message': error_message})

#     return render(request, 'agendar.html')
