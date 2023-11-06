from django.db import models

class Profissao(models.Model):
    nome_da_profissao = models.CharField(max_length=255)
    descricao = models.TextField()  # Adicionando um campo de descrição da profissão
    salario_medio = models.DecimalField(max_digits=10, decimal_places=2)  # Adicionando um campo para o salário médio
    requisitos = models.TextField()  # Adicionando um campo para os requisitos da profissão

    def __str__(self):
        return self.nome_da_profissao
