from django.contrib import admin

from arvore.models import Pais, Tios, Irmaos

admin.site.register(Tios)
admin.site.register(Pais)
admin.site.register(Irmaos)
