from django.db import models

from .irmaos import Irmaos
from .escolaridade import Escolaridade

class Tios(models.Model):
    nome_completo = models.CharField(max_length=255)
    data_de_nascimento = models.DateField()
    cidade_natal = models.CharField(max_length=255)
    primos = models.ManyToManyField(Irmaos, related_name='filhos')
    escolaridade = models.ForeignKey(Escolaridade, on_delete=models.PROTECT, related_name='tios_escolaridade')

    def __str__(self):
        return self.nome_completo
