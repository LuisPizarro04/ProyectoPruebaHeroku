from django import forms
from .models import Profesionale


class ProfesionaleForm(forms.ModelForm):
    class Meta:
        model = Profesionale
        fields = ['rut', 'nombres', 'apellidos', 'especialidad', 'edad', 'sexo', 'nacionalidad',
                  'ciudad_nacimiento', 'fecha_nacimiento', 'direccion', 'estado']

        labels = {
            'rut': 'Rut del Profesional',
            'nombres': 'Nombres del Profesional',
            'apellidos': 'Apellidos del Profesional',
            'especialidad': 'Especialidad del Profesional',
            'edad': 'Edad del Profesional',
            'sexo': 'Sexo del Profesional',
            'nacionalidad': 'Nacionalidad del Profesional',
            'ciudad_nacimiento': 'Ciudad',
            'fecha_nacimiento': 'Fecha de nacimiento del Profesional',
            'direccion': 'Dirección del Profesional',
            'estado': 'Estado Profesional',
        }
        widgets = {
            'rut': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese...',
                    'id': 'rut',
                }
            ),
            'nombres': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese...',
                    'id': 'nombres',
                }
            ),
            'apellidos': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese...',
                    'id': 'apellidos',
                }
            ),
            'especialidad': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese...',
                    'id': 'especialidad',
                }
            ),
            'edad': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese...',
                    'id': 'edad',
                }
            ),
            'sexo': forms.Select(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese...',
                    'id': 'sexo',
                }
            ),
            'nacionalidad': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese...',
                    'id': 'nacionalidad',
                }
            ),
            'ciudad_nacimiento': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese...',
                    'id': 'ciudad_nacimiento',
                }
            ),
            'fecha_nacimiento': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese...',
                    'id': 'fecha_nacimiento',
                }
            ),
            'direccion': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese...',
                    'id': 'direccion',
                }
            ),
            'estado': forms.Select(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Seleccione...',
                    'id': 'estado',
                }
            ),
        }
