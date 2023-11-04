from rest_framework.serializers import ModelSerializer
from arvore.models import Pais

class PaisSerializer(ModelSerializer):
    class Meta:
        model = Pais
        fields = "__all__"