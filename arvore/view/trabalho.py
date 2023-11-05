from rest_framework.viewsets import ModelViewSet

from arvore.models import Trabalho
from arvore.serializer import TrabalhoSerializer

class TrabalhoViewSet(ModelViewSet):
    queryset = Trabalho.objects.all()
    serializer_class = TrabalhoSerializer