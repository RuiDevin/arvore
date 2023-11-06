from django.db import models

class Escolaridade(models.Model):
    nome_da_escola = models.CharField(max_length=255)

    ESCOLARIDADES_CHOICES = (
        ('EF completo', 'Ensino Fundamental Completo'),
        ('EF incompleto', 'Ensino Fundamental Incompleto'),
        ('EM completo', 'Ensino Medio Completo'),
        ('EM incompleto', 'Ensino Medio Incompleto'),
        ('Graduação', 'Graduando'),
        ('Pos-graduação', 'Pos-graduação'),
    )
    
    nivel_escolaridade = models.CharField(max_length=20, choices=ESCOLARIDADES_CHOICES)

    def __str__(self):
        return self.nivel_escolaridade