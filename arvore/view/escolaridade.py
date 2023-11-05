from rest_framework.viewsets import ModelViewSet

from arvore.models import Escolaridade
from arvore.serializer import EscolaridadeSerializer

class EscolaridadeViewSet(ModelViewSet):
    queryset = Escolaridade.objects.all()
    serializer_class = EscolaridadeSerializer