from rest_framework import viewsets, filters
from .models import Dueno, Mascota
from .serializers import DuenoSerializer, MascotaSerializer


class DuenoViewSet(viewsets.ModelViewSet):
    queryset = Dueno.objects.all()
    serializer_class = DuenoSerializer


class MascotaViewSet(viewsets.ModelViewSet):
    queryset = Mascota.objects.all()
    serializer_class = MascotaSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['nombre', 'especie']