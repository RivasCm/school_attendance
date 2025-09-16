# evaluacion/models.py
from django.db import models
from personal.models import Alumno
from school.models import Materia
from personal.models import Profesor


class Nota(models.Model):
    id_alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    id_materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    ser = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    saber = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    hacer = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    decidir = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    calificacion_trimestral = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    observaciones = models.TextField(blank=True, null=True)
    
    class Meta:
        verbose_name_plural = "Notas"
        unique_together = ('id_alumno', 'id_materia')

    def __str__(self):
        return f"{self.id_alumno.nombre} - {self.id_materia.nombre_materia}"


class Asistencia(models.Model):
    id_alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    id_materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    fecha_clase = models.DateField()
    estado = models.CharField(max_length=1, choices=[
        ('A', 'Asistencia'),
        ('F', 'Falta'),
        ('R', 'Retraso'),
        ('L', 'Licencia'),
    ])

    class Meta:
        verbose_name_plural = "Asistencias"
        unique_together = ('id_alumno', 'id_materia', 'fecha_clase')

    def __str__(self):
        return f"{self.id_alumno.nombre} - {self.fecha_clase} - {self.estado}"

class ProfesorMateriaCurso(models.Model):
    id_profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    id_materia = models.ForeignKey(Materia, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id_profesor.nombre} - {self.id_materia.nombre_materia}'