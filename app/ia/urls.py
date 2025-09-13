# ia/urls.py
from django.urls import path
from .views import AgruparAlumnosView

urlpatterns = [
    path('agrupar/', AgruparAlumnosView.as_view(), name='agrupar-alumnos'),
]