from rest_framework import serializers
from .models import Dueno, Mascota


class DuenoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dueno
        fields = '__all__'


class MascotaSerializer(serializers.ModelSerializer):
    nombre_dueno = serializers.CharField(source='dueno.nombre', read_only=True)
    telefono_dueno = serializers.CharField(source='dueno.telefono', read_only=True)

    class Meta:
        model = Mascota
        fields = [
            'id',
            'nombre',
            'especie',
            'edad',
            'dueno',
            'nombre_dueno',
            'telefono_dueno'
        ]
