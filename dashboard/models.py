from django.db import models

# Create your models here.
class Carrera(models.Model):
    nombre = models.CharField(max_length=100)
    ciclos = models.ManyToManyField('Ciclo',related_name='carreras')
class Alumno(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    email = models.EmailField()
    celular = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    cursos = models.ManyToManyField('Curso')
    carrera = models.ForeignKey(Carrera,on_delete=models.CASCADE)
    def __str__(self):
        return self.name + " " + self.lastname
class Profesor(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    email = models.EmailField()
    celular = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name + " " + self.lastname
class Roles(models.Model):
    ADMIN = 'admin'
    ALUMNO= 'alumno'
    ROL_CHOICES = [
        (ADMIN,'Admin'),
        (ALUMNO,'Alumno')
    ]
    nombre = models.CharField(max_length=100,choices=ROL_CHOICES)

class Cuenta(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    alumno = models.OneToOneField(Alumno,on_delete=models.CASCADE)
    profesor = models.OneToOneField(Profesor,on_delete=models.CASCADE)
    rol = models.ForeignKey(Roles,on_delete=models.CASCADE)


class Ciclo(models.Model):
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)
    numero = models.IntegerField()

class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    ciclo = models.ForeignKey(Ciclo, on_delete=models.CASCADE)
    alumnos = models.ManyToManyField('Alumno')
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)

