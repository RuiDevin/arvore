from rest_framework.serializers import ModelSerializer
from arvore.models import Primos

class PrimosSerializer(ModelSerializer):
    class Meta:
        model = Primos
        fields = "__all__"