from django.contrib import admin
from .models import *


class ProfesionaleAdmin(admin.ModelAdmin):
    list_display = ("nombres", "apellidos", "edad", "nacionalidad", "especialidad")


admin.site.register(Profesionale, ProfesionaleAdmin)
