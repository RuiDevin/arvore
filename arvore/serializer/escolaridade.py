from rest_framework.serializers import ModelSerializer
from arvore.models import Escolaridade

class EscolaridadeSerializer(ModelSerializer):
    class Meta:
        model = Escolaridade
        fields = "__all__"
