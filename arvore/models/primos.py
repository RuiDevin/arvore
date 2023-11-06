from django.db import models

from .escolaridade import Escolaridade

class Primos(models.Model):
    nome_completo = models.CharField(max_length=255)
    data_de_nascimento = models.DateField()
    cidade_natal = models.CharField(max_length=255)
    pai = models.CharField(max_length=255)
    mae = models.CharField(max_length=255)
    escolaridade = models.ForeignKey(Escolaridade, on_delete=models.PROTECT, related_name='primos_escolaridade')

    def __str__(self):
        return self.nome_completo
