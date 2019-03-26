from rest_framework import viewsets
from .serializers import MascotaSerializer, EstadoSerializer
from Mascotas.models import Mascota, Estado

# Create your views here.
class MascotaViewSet(viewsets.ModelViewSet):
    """
    API endpoint que permite editar o visualizar una mascota
    """
    queryset = Mascota.objects.all()
    serializer_class = MascotaSerializer

class EstadoViewSet(viewsets.ModelViewSet):
    """
    API endpoint que permite editar o visualizar un estado
    """
    queryset = Estado.objects.all()
    serializer_class = EstadoSerializer
