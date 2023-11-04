from rest_framework.viewsets import ModelViewSet

from arvore.models import Tios
from arvore.serializer import TiosSerializer

class TiosViewSet(ModelViewSet):
    queryset = Tios.objects.all()
    serializer_class = TiosSerializer