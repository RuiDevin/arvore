from django.db import models

from .endereco import Endereco

class Trabalho(models.Model):
    endereço = models.ManyToManyField(Endereco,related_name='endereco')
    