from django.db import models

class Irmaos(models.Model):
    nome_completo = models.CharField(max_length=255)
    data_de_nascimento = models.DateField()
    cidade_natal = models.CharField(max_length=255)
    pai = models.CharField(max_length=255)
    mae = models.CharField(max_length=255)

    def __str__(self):
        return self.nome_completo
