# evaluacion/views.py
from rest_framework import viewsets
from .models import Nota, ProfesorMateriaCurso, Asistencia
from .serializers import NotaSerializer, ProfesorMateriaCursoSerializer, AsistenciaSerializer

class NotaViewSet(viewsets.ModelViewSet):
    queryset = Nota.objects.all()
    serializer_class = NotaSerializer
    
class ProfesorMateriaCursoViewSet(viewsets.ModelViewSet):
    queryset = ProfesorMateriaCurso.objects.all()
    serializer_class = ProfesorMateriaCursoSerializer

class AsistenciaViewSet(viewsets.ModelViewSet):
    queryset = Asistencia.objects.all()
    serializer_class = AsistenciaSerializer