from Mascotas.models import Mascota, Estado
from rest_framework import serializers


class EstadoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Estado
        fields = ('descripcion')

class MascotaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Mascota
        fields = ('nombre', 'fotografia', 'raza', 'descripcion', 'estado')