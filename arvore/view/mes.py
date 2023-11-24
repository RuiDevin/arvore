from rest_framework.viewsets import ModelViewSet

from arvore.models import Mes
from arvore.serializer import MesSerializer

class MesViewSet(ModelViewSet):
    queryset = Mes.objects.all()
    serializer_class = MesSerializer