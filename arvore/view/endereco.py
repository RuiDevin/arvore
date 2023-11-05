from rest_framework.viewsets import ModelViewSet

from arvore.models import Endereco
from arvore.serializer import EnderecoSerializer

class EnderecoViewSet(ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer