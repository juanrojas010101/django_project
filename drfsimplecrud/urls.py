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
from apipaciente.views import EliminarMiModelo
from apiespecialidad.views import EliminarEspecialidad
from models.views import EliminarMedico
from apipaciente.views import ActualizarPaciente


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('projects.urls')),
    path('models/', include('models.urlsModels')),
    path('paciente/', include('apipaciente.urlspaciente')),
    path('especialidad/', include('apiespecialidad.urlsespecialidad')),
    path('eliminarPaciente/<int:pk>/', EliminarMiModelo.as_view(), name='eliminar_mimodelo'),
    path('eliminarEspecialidad/<int:pk>/', EliminarEspecialidad.as_view(), name='eliminar_mimodelo'),
    path('eliminarMedico/<int:pk>/', EliminarMedico.as_view(), name='eliminar_mimodelo'),
     path('articulos/<int:pk>/', ActualizarPaciente.as_view(), name='ver-actualizar-articulo'),
]
   

