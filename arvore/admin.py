from django.contrib import admin

from arvore.models import Pais, Tios, Irmaos,Primos, Endereco, Escolaridade, Profissao, Mes

admin.site.register(Tios)
admin.site.register(Pais)
admin.site.register(Irmaos)
admin.site.register(Primos)
admin.site.register(Endereco)
admin.site.register(Escolaridade)
admin.site.register(Profissao)
admin.site.register(Mes)
