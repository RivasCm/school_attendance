# personal/views.py
from rest_framework import viewsets
from .models import Profesor, Alumno
from .serializers import ProfesorSerializer, AlumnoSerializer

class ProfesorViewSet(viewsets.ModelViewSet):
    queryset = Profesor.objects.all()
    serializer_class = ProfesorSerializer

class AlumnoViewSet(viewsets.ModelViewSet):
    queryset = Alumno.objects.all()
    serializer_class = AlumnoSerializer