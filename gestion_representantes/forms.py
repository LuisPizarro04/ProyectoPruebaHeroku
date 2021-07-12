from django import forms
from .models import Representante


class RepresentanteForm(forms.ModelForm):
    class Meta:
        model = Representante
        fields = ['rut', 'nombres', 'apellidos', 'edad', 'sexo', 'nacionalidad',
                  'ciudad_nacimiento', 'fecha_nacimiento', 'direccion', 'estado']
        labels = {
            'rut': 'Rut del Representante',
            'nombres': 'Nombres del Representante',
            'apellidos': 'Apellidos del Representante',
            'edad': 'Edad del Representante',
            'sexo': 'Sexo del Representante',
            'nacionalidad': 'Nacionalidad del Representante',
            'ciudad_nacimiento': 'Ciudad',
            'fecha_nacimiento': 'Fecha de nacimiento del Representante',
            'direccion': 'Dirección del Representante',
            'estado': 'Estado Representante',
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
                    'placeholder': 'Seleccione...',
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
