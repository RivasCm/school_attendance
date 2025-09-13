# personal/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProfesorViewSet, AlumnoViewSet

router = DefaultRouter()
router.register(r'profesores', ProfesorViewSet)
router.register(r'alumnos', AlumnoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]