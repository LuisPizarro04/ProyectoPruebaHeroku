from django.contrib import admin
from .models import Cita


class CitaAdmin(admin.ModelAdmin):
    list_display = ("representante", "correo", "especialista", "hora_atencion", "fecha_atencion")


admin.site.register(Cita, CitaAdmin)
