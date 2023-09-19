from rest_framework import serializers
from .models import Horario, Opcion

class HorarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Horario
        fields = '__all__'

class OpcionSerializer(serializers.ModelSerializer):
    horario = HorarioSerializer(many=True)
    class Meta:
        model = Opcion
        fields = '__all__'