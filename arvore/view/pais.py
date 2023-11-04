from rest_framework.viewsets import ModelViewSet

from arvore.models import Pais
from arvore.serializer import PaisSerializer

class PaisViewSet(ModelViewSet):
    queryset = Pais.objects.all()
    serializer_class = PaisSerializer