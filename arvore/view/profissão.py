from rest_framework.viewsets import ModelViewSet

from arvore.models import Profissao
from arvore.serializer import ProfissaoSerializer

class ProfissaoViewSet(ModelViewSet):
    queryset = Profissao.objects.all()
    serializer_class = ProfissaoSerializer