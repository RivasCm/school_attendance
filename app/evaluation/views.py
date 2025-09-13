# evaluacion/views.py
from rest_framework import viewsets
from .models import Nota, Dimension, ProfesorMateriaCurso
from .serializers import NotaSerializer, DimensionSerializer, ProfesorMateriaCursoSerializer

class NotaViewSet(viewsets.ModelViewSet):
    queryset = Nota.objects.all()
    serializer_class = NotaSerializer

class DimensionViewSet(viewsets.ModelViewSet):
    queryset = Dimension.objects.all()
    serializer_class = DimensionSerializer

class ProfesorMateriaCursoViewSet(viewsets.ModelViewSet):
    queryset = ProfesorMateriaCurso.objects.all()
    serializer_class = ProfesorMateriaCursoSerializer