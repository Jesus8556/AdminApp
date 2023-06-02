from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import DeleteView
from django.urls import reverse_lazy

from dashboard.forms import AlumnoForm,ProfesorForm
from .models import *
from .forms import *
from django.http.response import JsonResponse
from django_dyn_dt.datatb import DataTB
from django.shortcuts import render
from .models import Carrera
from django.contrib.auth import logout

# Create your views here.
from django.contrib.auth.decorators import login_required

@login_required
def BASE(request):
    return render(request, 'home.html')

def opcion(request):
    return render(request,'opcionAlumno.html' )

def index(request):
    return render (request, 'tblAlumno.html')
class AlumnoView(View):
    
    def get(self,request):
        listaAlumnos = Alumno.objects.all()
        formAlumno = AlumnoForm()
        context = {
            'alumnos' : listaAlumnos,
            'formAlumno': formAlumno
        }
        return render(request,'tblAlumno.html',context)
    def post(self, request, pk = None):
        
    
        formAlumno = AlumnoForm(request.POST)
        if formAlumno.is_valid():
            formAlumno.save()
            return redirect('/listaAlumno')
class ProfesorView(View):
    
    def get(self,request):
        listaProfesores = Profesor.objects.all()
        formProfesor = ProfesorForm()
        context = {
            'profesores' : listaProfesores,
            'formProfesor': formProfesor
        }
        return render(request,'tblProfesor.html',context)


class CursoView(View):
    
    def get(self,request):
        listaCursos = Curso.objects.all()
        formCurso = CursoForm()
        context = {
            'cursos' : listaCursos,
            'formCurso': formCurso
        }
        return render(request,'tblCurso.html',context)


class CuentaView(View):
    
    def get(self,request):
        listaCuentas = Cuenta.objects.all()
        formCuenta = CuentaForm()
        context = {
            'cuentas' : listaCuentas,
            'formCuenta': formCuenta
        }
        return render(request,'tblCuenta.html',context)


def alumnos_por_curso(request):
    cursos = Curso.objects.all()  
    contexto = {'cursos': cursos}  
    return render(request, 'alumnos_por_curso.html', contexto)

def lista_carreras(request):
    carreras = Carrera.objects.all()  
    contexto = {'carreras': carreras}  
    return render(request, 'carreras.html', contexto)

def salir(request):
    logout(request)
    return redirect('/')