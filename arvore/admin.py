from django.contrib import admin

from arvore.models import Pais, Tios, Irmao

admin.site.register(Tios)
admin.site.register(Pais)
admin.site.register(Irmao)
