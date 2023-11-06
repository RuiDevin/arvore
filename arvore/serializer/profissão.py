from rest_framework.serializers import ModelSerializer
from arvore.models import Profissao

class ProfissaoSerializer(ModelSerializer):
    class Meta:
        model = Profissao
        fields = "__all__"