from django import forms
from .models import Calendario


class DateInput(forms.DateInput):
    input_type = 'date'


class TimeInput(forms.TimeInput):
    input_type = 'time'


class CalendarioForm(forms.ModelForm):
    class Meta:
        model = Calendario
        fields = ['fecha_reserva', 'hora_reserva', 'estado', 'profesional', 'especialidad']
        labels = {
            'fecha_reserva': 'Fecha reserva',
            'hora_reserva': 'Hora reserva',
            'estado': 'Estado reserva',
            'profesional': 'Profesional a cargo',
            'especialidad': 'Especilidad',
        }
        widgets = {
            'fecha_reserva': DateInput(),
            'hora_reserva': TimeInput(),
            'estado': forms.Select(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Seleccione estado',
                    'id': 'estado',
                }
            ),
            'profesional': forms.Select(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Seleccione profesional',
                    'id': 'profesional',
                }
            ),
            'especialidad': forms.Select(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Selecione Especialidad',
                    'id': 'especialidad',
                }
            ),

        }
