# evaluacion/serializers.py
from rest_framework import serializers
from .models import Nota, Dimension, ProfesorMateriaCurso

class NotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nota
        fields = '__all__'

class DimensionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dimension
        fields = '__all__'

class ProfesorMateriaCursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfesorMateriaCurso
        fields = '__all__'