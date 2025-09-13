# ia/views.py
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
            # Obtener las notas del alumno para el trimestre
            # Excluimos la autoevaluación, ya que no está disponible
            notas_alumno = Nota.objects.filter(id_alumno=alumno)
            
            # Calcular el promedio de las dimensiones relevantes
            ser_promedio = np.mean([nota.ser for nota in notas_alumno if nota.ser is not None]) if notas_alumno else 0
            saber_promedio = np.mean([nota.saber for nota in notas_alumno if nota.saber is not None]) if notas_alumno else 0
            hacer_promedio = np.mean([nota.hacer for nota in notas_alumno if nota.hacer is not None]) if notas_alumno else 0
            
            # Crear un vector de características para K-Means
            data.append([ser_promedio, saber_promedio, hacer_promedio])
        
        # 2. Convertir los datos a un array de NumPy
        if not data:
            return Response({'error': 'No hay datos de alumnos para agrupar.'}, status=status.HTTP_404_NOT_FOUND)
            
        X = np.array(data)

        # 3. Implementar y entrenar el modelo K-Means
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