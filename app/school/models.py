# colegio/models.py
from django.db import models

class Especialidad(models.Model):
    id_especialidad = models.AutoField(primary_key=True)
    nombre_especialidad = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.nombre_especialidad

class Curso(models.Model):
    id_curso = models.AutoField(primary_key=True)
    nombre_curso = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.nombre_curso

class Materia(models.Model):
    id_materia = models.AutoField(primary_key=True)
    nombre_materia = models.CharField(max_length=100, unique=True)
    id_curso = models.ForeignKey(Curso, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.nombre_materia