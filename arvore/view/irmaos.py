from rest_framework.viewsets import ModelViewSet

from arvore.models import Irmaos
from arvore.serializer import IrmaosSerializer

class IrmaosViewSet(ModelViewSet):
    queryset = Irmaos.objects.all()
    serializer_class = IrmaosSerializer