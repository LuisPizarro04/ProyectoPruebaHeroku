from django.contrib import admin
from .models import Paciente, Ficha


class PacienteAdmin(admin.ModelAdmin):
    list_display = ("nombres", "apellidos", "edad", "nacionalidad", "representante")


class FichaAdmin(admin.ModelAdmin):
    list_display = ("nombres", "apellidos", "especialidad", "hora_atencion", "fecha_atencion")

admin.site.register(Paciente, PacienteAdmin)
admin.site.register(Ficha, FichaAdmin)
