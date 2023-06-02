from django.db import models
from django.forms import ValidationError

from .models import *



# Create your models here.
class Roles(models.Model):
    ADMIN = 'admin'
    ALUMNO = 'alumno'
    ROL_CHOICES = [
        (ADMIN, 'Admin'),
        (ALUMNO, 'Alumno')
    ]
    nombre = models.CharField(max_length=100, choices=ROL_CHOICES)
    def __str__(self):
        return self.nombre 



class Cuenta(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    
    rol = models.ForeignKey(Roles, on_delete=models.CASCADE)
    def __str__(self):
        return self.username

class Carrera(models.Model):
    nombre = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre
    
class Ciclo(models.Model):
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)
    numero = models.IntegerField()
    def __str__(self):
        return f"Ciclo {self.numero} - {self.carrera.nombre}"

    class Meta:
        unique_together = ('carrera', 'numero')

    def clean(self):
        if self.numero < 1 or self.numero > 6:
            raise ValidationError("El número del ciclo debe estar entre 1 y 6.")




class Alumno(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    email = models.EmailField()
    celular = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    ciclo = models.ForeignKey(Ciclo, on_delete=models.CASCADE, null=True)
    cuenta = models.OneToOneField(Cuenta, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.nombre + " " + self.apellido


class Profesor(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    email = models.EmailField()
    celular = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    cuenta = models.OneToOneField(Cuenta, on_delete=models.CASCADE, null=True)
    

    def __str__(self):
        return self.nombre + " " + self.apellido





class Aula(models.Model):
    nombre = models.CharField(max_length=100)
    cursos = models.ManyToManyField('Curso', blank=True)
    def __str__(self):
        return self.nombre


class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    ciclo = models.ForeignKey(Ciclo, on_delete=models.CASCADE)
    alumnos = models.ManyToManyField('Alumno')
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    aulas = models.ManyToManyField('Aula')
    def __str__(self):
        return self.nombre

    
    def crear_notas_laboratorio(self):
        for numero in range(1, 17):
            NotaLaboratorio.objects.create(curso=self, numero=numero)
    

class NotaLaboratorio(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    numero = models.IntegerField()
    nombre = models.CharField(max_length=100)


class Horario(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    dia = models.DateField()
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()

    def __str__(self):
        return f"Horario - Curso: {self.curso.nombre}, Día: {self.dia}, Hora inicio: {self.hora_inicio}, Hora fin: {self.hora_fin}"
