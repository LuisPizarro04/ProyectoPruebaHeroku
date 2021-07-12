from django import forms
from .models import Paciente, Ficha


class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['representante', 'parentesco', 'grado', 'rut', 'nombres', 'apellidos', 'edad', 'sexo', 'nacionalidad',
                  'ciudad_nacimiento', 'fecha_nacimiento', 'direccion', 'estado']
        labels = {
            'representante': 'Nombre del representante',
            'parentesco': 'Parentesco con el paciente',
            'grado': 'Grado TEA del paciente',
            'rut': 'Rut del paciente',
            'nombres': 'Nombres del paciente',
            'apellidos': 'Apellidos del paciente',
            'edad': 'Edad del paciente',
            'sexo': 'Sexo del paciente',
            'nacionalidad': 'Nacionalidad del paciente',
            'ciudad_nacimiento': 'Ciudad',
            'fecha_nacimiento': 'Fecha de nacimiento del paciente',
            'direccion': 'Dirección del paciente',
            'estado': 'Estado paciente',
        }
        widgets = {
            'representante': forms.Select(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Seleccione...',
                    'id': 'representante',
                }
            ),
            'parentesco': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese...',
                    'id': 'parentesco'
                }
            ),
            'grado': forms.Select(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Seleccione',
                    'id': 'grado',
                }
            ),
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


class FichaForm(forms.ModelForm):
    class Meta:
        model = Ficha
        fields = ['representante', 'especialidad', 'rut', 'nombres', 'apellidos', 'hora_atencion', 'fecha_atencion']
        labels = {
            'representante': 'Nombre del representante',
            'especialidad': 'Nombre del especialista',
            'rut': 'Rut del paciente',
            'nombres': 'Nombres del paciente',
            'apellidos': 'Apellidos del paciente',
            'hora_atencion': 'Hora atencion del paciente',
            'fecha_atencion': 'Fecha atencion del paciente',
        }
        widgets = {
            'representante': forms.Select(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Seleccione...',
                    'id': 'representante',
                }
            ),
            'especialidad': forms.Select(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Seleccione...',
                    'id': 'especialidad',
                }
            ),
            'rut': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese...',
                    'id': 'rut'
                }
            ),
            'nombres': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese...',
                    'id': 'nombres'
                }
            ),
            'apellidos': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese...',
                    'id': 'apellidos'
                }
            ),
            'hora_atencion': forms.TimeInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese...',
                    'id': 'hora_atencion',
                }
            ),
            'fecha_atencion': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese...',
                    'id': 'fecha_atencion',
                }
            ),
        }
