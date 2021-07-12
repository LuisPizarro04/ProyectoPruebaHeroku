from django.contrib import admin
from .models import *


class RepresentanteAdmin(admin.ModelAdmin):
    list_display = ("nombres", "apellidos", "edad", "nacionalidad","contacto","correo")


admin.site.register(Representante, RepresentanteAdmin)

