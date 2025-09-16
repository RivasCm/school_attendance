# evaluacion/serializers.py
from rest_framework import serializers
from .models import Nota, ProfesorMateriaCurso, Asistencia

class NotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nota
        fields = ['id_alumno', 'id_materia', 'ser', 'saber', 'hacer', 'decidir', 'calificacion_trimestral', 'observaciones']

class ProfesorMateriaCursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfesorMateriaCurso
        fields = '__all__'

class AsistenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asistencia
        fields = ['id_alumno', 'id_materia', 'fecha_clase', 'estado']