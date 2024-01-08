from django.contrib import admin
from .models import Usuario, Categoria

admin.site.site_header = 'Sistema PDV'

admin.site.register(Usuario)
admin.site.register(Categoria)
