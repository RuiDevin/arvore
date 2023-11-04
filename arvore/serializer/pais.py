from rest_framework.serializers import ModelSerializer
from arvore.models import Pais

class PaisSerializer(ModelSerializer):
    class Meta:
        model = Pais
        field = "__all__"