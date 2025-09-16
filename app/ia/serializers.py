# proyecto_asistencia/ia/serializers.py
from rest_framework import serializers

class KMeansResultSerializer(serializers.Serializer):
    # Este serializador se usará para la respuesta del modelo de IA
    alumno_id = serializers.IntegerField()
    cluster = serializers.IntegerField()
    # Otros campos relevantes para la visualización del agrupamiento