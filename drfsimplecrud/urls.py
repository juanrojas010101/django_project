"""drfsimplecrud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from apiespecialidad.views import EliminarEspecialidad
from models.views import EliminarMedico
from models.views import ActualizarMedico
from apipaciente.views import ActualizarPaciente
from apipaciente.views import EliminarPaciente
from apiespecialidad.views import ActualizarEspecialidad
from ciudades.views import cargar_datos_desde_json


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('projects.urls')),
    path('models/', include('models.urlsModels')),
    path('paciente/', include('apipaciente.urlspaciente')),
    path('especialidad/', include('apiespecialidad.urlsespecialidad')),
    path('ciudades/', include('ciudades.urlsciudad')),
    path('cargar-datos/', cargar_datos_desde_json, name='cargar_datos'),
    path('eliminarPaciente/<int:pk>/', EliminarPaciente.as_view(), name='eliminar_mimodelo'),
    path('actualizarPaciente/<int:pk>/', ActualizarMedico.as_view(), name='ver-actualizar-articulo'),
    path('eliminarEspecialidad/<int:pk>/', EliminarEspecialidad.as_view(), name='eliminar_mimodelo'),
    path('articulos/<int:pk>/', ActualizarEspecialidad.as_view(), name='ver-actualizar-articulo'),
    path('eliminarMedico/<int:pk>/', EliminarMedico.as_view(), name='eliminar_mimodelo'),
    path('articulos/<int:pk>/', ActualizarPaciente.as_view(), name='ver-actualizar-articulo'),
]
   

