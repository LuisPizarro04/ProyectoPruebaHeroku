from django import forms
from .models import Cita


class DateInput(forms.DateInput):
    input_type = 'date'


class Cifaform(forms.ModelForm):
    class Meta:
        model = Cita
        fields = ['representante', 'correo', 'contacto', 'paciente', 'especialista', 'especialidad', 'hora_atencion',
                  'fecha_atencion', ]
        labels = {
            'representante': 'Nombre del representante',
            'correo': 'Correo del representante',
            'contacto': 'Contacto del representante',
            'paciente': 'Paciente a evaluar',
            'especialista': 'Especialista a cargo',
            'especialidad': 'Especialidad',
            'hora_atencion': 'Hora de atencion',
            'fecha_atencion': 'Fecha de atencion',
        }
        widgets = {
            'representante': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese...',
                    'id': 'representante',
                }
            ),
            'correo': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese...',
                    'id': 'correo',
                }
            ),
            'contacto': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese...',
                    'id': 'contacto',
                }
            ),
            'paciente': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese...',
                    'id': 'paciente',
                }
            ),
            'especialista': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese...',
                    'id': 'especialista',
                }
            ),
        }
