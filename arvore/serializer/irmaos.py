from rest_framework.serializers import ModelSerializer
from arvore.models import Irmaos

class IrmaosSerializer(ModelSerializer):
    class Meta:
        model = Irmaos
        field = "__all__"