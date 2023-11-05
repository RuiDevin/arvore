from django.db import models

class Endereco(models.Model):
    rua = models.CharField(max_length=255)
    bairro = models.CharField(max_length=255)
    numero = models.IntegerField()
    cidade = models.CharField(max_length=255)
    estado = models.CharField(max_length=255)
    ponto_de_referencia = models.CharField(max_length=255)
    cep = models.CharField(max_length=10) 

    def __str__(self):
        return f"{self.rua}, {self.cep}, {self.numero} - {self.cidade}, {self.estado}"
