from rest_framework.viewsets import ModelViewSet

from arvore.models import Primos
from arvore.serializer import PrimosSerializer

class PrimosViewSet(ModelViewSet):
    queryset = Primos.objects.all()
    serializer_class = PrimosSerializer