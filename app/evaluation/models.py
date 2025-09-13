# evaluacion/models.py
from django.db import models
from personal.models import Alumno
from school.models import Materia
from datetime import date

class Dimension(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nombre

class Nota(models.Model):
    TIPO_EVALUACION_CHOICES = [
        ('Examen', 'Examen'),
        ('Quiz', 'Quiz'),
        ('Tarea', 'Tarea'),
        ('Proyecto', 'Proyecto'),
        ('Participacion', 'Participacion'),
        ('Asistencia', 'Asistencia'),
    ]
    ASISTENCIA_CHOICES = [
        ('Presente', 'Presente'),
        ('Ausente', 'Ausente'),
        ('Tardanza', 'Tardanza'),
        ('Justificado', 'Justificado'),
    ]

    id_nota = models.AutoField(primary_key=True)
    id_alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    id_materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    tipo_evaluacion = models.CharField(max_length=50, choices=TIPO_EVALUACION_CHOICES, null=True)
    evaluacion = models.CharField(max_length=100, null=True, blank=True)
    nota = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    asistencia = models.CharField(max_length=50, choices=ASISTENCIA_CHOICES, null=True)
    fecha_evaluacion = models.DateField(default=date.today)
    observaciones = models.TextField(null=True, blank=True)

class ProfesorMateriaCurso(models.Model): # Se agregó esta tabla para la relación de 3
    id_pmc = models.AutoField(primary_key=True)
    id_profesor = models.ForeignKey('personal.Profesor', on_delete=models.CASCADE)
    id_materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    class Meta:
        unique_together = ('id_profesor', 'id_materia')