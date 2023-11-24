from django.db import models

from .endereco import Endereco
from .profissão import Profissao

ESCOLHAS_SALARIO_MINIMO = (
    ('Salário Mínimo 1994', '70 Reais (1994)'),
    ('Salário Mínimo 1995', '100 Reais (1995)'),
    ('Salário Mínimo 1996', '112 Reais (1996)'),
    ('Salário Mínimo 1997', '120 Reais (1997)'),
    ('Salário Mínimo 1998', '130 Reais (1998)'),
    ('Salário Mínimo 1999', '136 Reais (1999)'),
    ('Salário Mínimo 2000', '151 Reais (2000)'),
    ('Salário Mínimo 2001', '180 Reais (2001)'),
    ('Salário Mínimo 2002', '200 Reais (2002)'),
    ('Salário Mínimo 2003', '240 Reais (2003)'),
    ('Salário Mínimo 2004', '260 Reais (2004)'),
    ('Salário Mínimo 2005', '300 Reais (2005)'),
    ('Salário Mínimo 2006', '350 Reais (2006)'),
    ('Salário Mínimo 2007', '380 Reais (2007)'),
    ('Salário Mínimo 2008', '415 Reais (2008)'),
    ('Salário Mínimo 2009', '465 Reais (2009)'),
    ('Salário Mínimo 2010', '510 Reais (2010)'),
    ('Salário Mínimo 2011', '545 Reais (2011)'),
    ('Salário Mínimo 2012', '622 Reais (2012)'),
    ('Salário Mínimo 2013', '678 Reais (2013)'),
    ('Salário Mínimo 2014', '724 Reais (2014)'),
    ('Salário Mínimo 2015', '788 Reais (2015)'),
    ('Salário Mínimo 2016', '880 Reais (2016)'),
    ('Salário Mínimo 2017', '937 Reais (2017)'),
    ('Salário Mínimo 2018', '954 Reais (2018)'),
    ('Salário Mínimo 2019', '998 Reais (2019)'),
    ('Salário Mínimo 2020', '1045 Reais (2020)'),
    ('Salário Mínimo 2021', '1100 Reais (2021)'),
    ('Salário Mínimo 2022', '1212 Reais (2022)'),
    ('Salário Mínimo 2023', '1320 Reais (2023)'),
)

class Trabalho(models.Model):
    endereco_atual = models.ManyToManyField(Endereco, related_name='endereco_atual')
    profissao_atual = models.ManyToManyField(Profissao, related_name='sua_profissao_atual')
    salario_atual = models.CharField(max_length=25, null=False, blank=True, choices=())  # Adicione as opções aqui, se necessário
    recebo_salario_minimo = models.CharField(max_length=25, choices=ESCOLHAS_SALARIO_MINIMO, null=False, blank=True)

class AntigoTrabalho(models.Model):
    endereco = models.ManyToManyField(Endereco, related_name='endereco')
    profissao = models.ManyToManyField(Profissao, related_name='sua_profissao')
    salario = models.CharField(max_length=25, null=False, blank=True, choices=())  # Adicione as opções aqui, se necessário
    recebia_salario_minimo = models.CharField(max_length=25, choices=ESCOLHAS_SALARIO_MINIMO, null=False, blank=True)
