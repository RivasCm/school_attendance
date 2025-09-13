from django.shortcuts import render

# Create your views here.
# proyecto_asistencia/ia/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import numpy as np
from sklearn.cluster import KMeans
from personal.models import Alumno
from evaluation.models import Nota
from .serializers import KMeansResultSerializer

class AgruparAlumnosView(APIView):
    def get(self, request, format=None):
        # 1. Obtener los datos de la base de datos
        alumnos = Alumno.objects.all()
        data = []
        for alumno in alumnos:
            # Ejemplo de cómo obtener las notas y promediarlas
            notas = Nota.objects.filter(alumno=alumno)
            promedio_total = np.mean([nota.nota for nota in notas]) if notas else 0
            
            # Aquí pueden añadir más características (features) como asistencia
            # Por ahora, solo usaremos el promedio de notas como ejemplo
            data.append([promedio_total])
        
        # 2. Convertir los datos a un array de NumPy
        X = np.array(data)

        # 3. Implementar y entrenar el modelo K-Means
        # Se asume que k=3, pero puede ser dinámico
        kmeans_model = KMeans(n_clusters=3, random_state=0, n_init='auto')
        kmeans_model.fit(X)
        
        # 4. Obtener los resultados y prepararlos para la respuesta
        results = []
        for i, alumno in enumerate(alumnos):
            results.append({
                'alumno_id': alumno.id,
                'cluster': int(kmeans_model.labels_[i]),
            })

        serializer = KMeansResultSerializer(results, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)