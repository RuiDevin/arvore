from rest_framework.serializers import ModelSerializer
from arvore.models import Tios

class TiosSerializer(ModelSerializer):
    class Meta:
        model = Tios
        fields = "__all__"