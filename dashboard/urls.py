from django.contrib import admin
from django.urls import path
from . import views
from .views import alumnos_por_curso
from .views import lista_carreras

urlpatterns = [
    path('', views.BASE, name = 'BASE'),
    path('opcionAlumno/', views.opcion, name = 'opcion'),
    path('listaAlumno/', views.AlumnoView.as_view(),name='listalumno'),
    path('listaProfesor/', views.ProfesorView.as_view(),name='listprofesor'),
    path('listaCurso/', views.CursoView.as_view(),name='listcurso'),
    path('listaCuenta/', views.CuentaView.as_view(),name='listcuenta'),
    path('alumnos_por_curso/', alumnos_por_curso, name='alumnos_por_curso'),
    path('lista_carreras/', lista_carreras, name='lista_carreras'),
    path('salir/', views.salir , name='salir')
]
