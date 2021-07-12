from django.db import models


class Cita(models.Model):
    id = models.AutoField(primary_key=True)
    representante = models.CharField('nombre representante', max_length=200, null=False, blank=False)
    correo = models.EmailField(max_length=150)
    contacto = models.CharField('contacto', max_length=12, null=False, blank=False)
    paciente = models.CharField('nombre paciente', max_length=200, null=False, blank=False)
    especialista = models.CharField('nombre especialista', max_length=200, null=False, blank=False)
    especialidad = models.CharField('Especialidad', max_length=200, null=True, blank=True)
    hora_atencion = models.TimeField(null=True, blank=True)
    fecha_atencion = models.DateField(null=True, blank=True)


class Meta:
    verbose_name = 'Cita'
    verbose_name_plural = 'Citas'


def __str__(self):
    return self.representante + " " + self.paciente + " " + self.especialista
