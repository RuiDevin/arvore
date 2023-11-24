from rest_framework.serializers import ModelSerializer
from arvore.models import Mes

class MesSerializer(ModelSerializer):
    class Meta:
        model = Mes
        fields = "__all__"
