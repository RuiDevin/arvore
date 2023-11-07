from django.db import models

from .endereco import Endereco
from .profissão import Profissao

class Trabalho(models.Model):
    endereço = models.ManyToManyField(Endereco,related_name='endereco')
    profissao = models.ManyToManyField(Profissao, related_name='sua_profissao' )