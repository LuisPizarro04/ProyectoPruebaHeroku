from django.db import models
from gestion_profesionales.models import Profesionale


# Create your models here.

class Calendario(models.Model):
    LIBRE = '0'
    OCUPADA = '1'

    ESTADO_CHOICES = [(LIBRE, 'Libre'), (OCUPADA, 'Ocupada'), ]

    ESP_1 = 'Fonoaudilogo'
    ESP_2 = 'Terapeuta Ocupacional'
    ESP_3 = 'Psicologo'

    ESPECIALIDAD_CHOICES = [(ESP_1, 'Fonoaudilogo'), (ESP_2, 'Terapeuta'), (ESP_3, 'Psicologo'), ]

    fecha_reserva = models.DateField('Fecha de reserva')
    hora_reserva = models.TimeField('Hora de reserva')
    estado = models.CharField('Estado reserva', max_length=1, choices=ESTADO_CHOICES, default=LIBRE)
    profesional = models.ForeignKey('gestion_profesionales.Profesionale', on_delete=models.CASCADE)
    especialidad = models.CharField(max_length=100, choices=ESPECIALIDAD_CHOICES, default=None)

    def __str__(self):
        return f'{self.fecha_reserva}'
