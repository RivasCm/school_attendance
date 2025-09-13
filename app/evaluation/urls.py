# evaluacion/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NotaViewSet, ProfesorMateriaCursoViewSet, AsistenciaViewSet

router = DefaultRouter()
router.register(r'notas', NotaViewSet)
router.register(r'profesor-materia-curso', ProfesorMateriaCursoViewSet)
router.register(r'asistencias', AsistenciaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]