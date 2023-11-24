from django.db import models

from .endereco import Endereco
from .profissão import Profissao

SALARIO_MINIMO_CHOICES = (
    ('salario_1994', '70_Reais'),
    ('salario_1995', '100_Reais'),
    ('salario_1996', '112_Reais'),
    ('salario_1997', '120_Reais'),
    ('salario_1998', '130_Reais'),
    ('salario_1999', '136_Reais'),
    ('salario_2000', '151_reais'),
    ('salario_2001', '180_reais'),
    ('salario_2002', '200_reais'),
    ('salario_2003', '240_reais'),
    ('salario_2004', '260_reais'),
    ('salario_2005', '300_reais'),
    ('salario_2006', '350_reais'),
    ('salario_2007', '380_reais'),
    ('salario_2008', '415_reais'),
    ('salario_2009', '465_reais'),
    ('salario_2010', '510_reais'),
    ('salario_2011', '545_reais'),
    ('salario_2012', '622_reais'),
    ('salario_2013', '678_reais'),
    ('salario_2014', '724_reais'),
    ('salario_2015', '788_reais'),
    ('salario_2016', '880_reais'),
    ('salario_2017', '937_reais'),
    ('salario_2018', '954_reais'),
    ('salario_2019', '998_reais'),
    ('salario_2020', '1045_reais'),
    ('salario_2021', '1100_reais'),
    ('salario_2022', '1212_reais'),
    ('salario_2023', '1320_reais'),
)


class Trabalho(models.Model):
    endereço = models.ManyToManyField(Endereco,related_name='endereco')
    profissao = models.ManyToManyField(Profissao, related_name='sua_profissao' )
    salario = models.CharField(max_length=25, choices=SALARIO_MINIMO_CHOICES, null=True)

    