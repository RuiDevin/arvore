from django.db import models

MESES_DO_ANO = [
    ('Jn', 'Janeiro'),
    ('Fv', 'Fevereiro'),
    ('Mar', 'Março'),
    ('Abr', 'Abril'),
    ('Mai', 'Maio'),
    ('Jun', 'Junho'),
    ('Jul', 'Julho'),
    ('Ag', 'Agosto'),
    ('Set', 'Setembro'),
    ('Out', 'Outubro'),
    ('Nov', 'Novembro'),
    ('Dez', 'Dezembro'),
]

class Mes(models.Model):
    mes_do_ano = models.CharField(max_length=255, choices=MESES_DO_ANO, null=True)

    def __str__(self):
        return self.mes_do_ano