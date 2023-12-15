from rest_framework import serializers
from .models import Atleta, Evento

#Convierte un modelo en datos que pueden ser consultados (JSON)
class AtletaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Atleta
        fields = '__all__'

class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = '__all__'