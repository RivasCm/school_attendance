# evaluacion/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NotaViewSet, DimensionViewSet, ProfesorMateriaCursoViewSet

router = DefaultRouter()
router.register(r'notas', NotaViewSet)
router.register(r'dimensiones', DimensionViewSet)
router.register(r'profesor-materia-curso', ProfesorMateriaCursoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]