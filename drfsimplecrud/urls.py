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
from medico.views import EliminarMedico
from medico.views import ActualizarMedico
from apipaciente.views import ActualizarPaciente
from apipaciente.views import EliminarPaciente
from apiespecialidad.views import ActualizarEspecialidad
from ciudades.views import cargar_datos_desde_json
#from models import views
#from models.views import obtener_ids
#from projects.views import obtener_registros
#from models.views import consulta_medicos
from django.urls import path 
#from login.views import login_view
#from login.views import LoginView
from django.urls import path
from knox import views as knox_views
from login.views import LoginAPI

#asi deberia funcionar asi lo tengo la cosa es que no se quiere instalar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('projects.urls')),
    path('medico/', include('medico.urlsMedico')),
    path('agendar/', include('agendar.urls')),
    path('paciente/', include('apipaciente.urlspaciente')),
    path('especialidad/', include('apiespecialidad.urlsespecialidad')),
    path('ciudades/', include('ciudades.urlsciudad')),
    path('soporte/', include('soporte.urls')),
    #path('consulta/', consulta_medicos, name='consulta_medicos'),
    path('cargar-datos/', cargar_datos_desde_json, name='cargar_datos'),
    path('eliminarPaciente/<int:pk>/', EliminarPaciente.as_view(), name='eliminar_mimodelo'),
    path('actualizarPaciente/<int:pk>/', ActualizarMedico.as_view(), name='ver-actualizar-articulo'),
    path('eliminarEspecialidad/<int:pk>/', EliminarEspecialidad.as_view(), name='eliminar_mimodelo'),
    path('articulos/<int:pk>/', ActualizarEspecialidad.as_view(), name='ver-actualizar-articulo'),
    path('eliminarMedico/<int:pk>/', EliminarMedico.as_view(), name='eliminar_mimodelo'),
    path('articulos/<int:pk>/', ActualizarPaciente.as_view(), name='ver-actualizar-articulo'),
    # path('api/login/', LoginView.as_view(), name='login'),
    # path('login/', include('login.urls')),
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
]


