from django.db import models

from .escolaridade import Escolaridade
from .endereco import Endereco
from .trabalho import Trabalho

class Irmaos(models.Model):
    nome_completo = models.CharField(max_length=255)
    data_de_nascimento = models.DateField()
    endereco = models.ManyToManyField(Endereco,related_name='endereco_irmao')
    escolaridade = models.ForeignKey(Escolaridade, on_delete=models.PROTECT, related_name='escolaridade')
    trabalho = models.ManyToManyField(Trabalho,related_name='suas_profissoes')
    pai = models.CharField(max_length=255)
    mae = models.CharField(max_length=255)

    def __str__(self):
        return self.nome_completo
