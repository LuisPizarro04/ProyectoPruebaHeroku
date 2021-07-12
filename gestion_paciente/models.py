from django.db import models
from gestion_representantes.models import Representante
from gestion_profesionales.models import Profesionale


class Paciente(models.Model):
    id = models.AutoField(primary_key=True)
    representante = models.ForeignKey('gestion_representantes.Representante', on_delete=models.CASCADE)
    parentesco = models.CharField('parentesco', max_length=12, null=False, blank=False)
    grados = [("1", "Grado1"), ("2", "Grado2"), ("3", "Grado3")]
    grado = models.CharField(max_length=100, null=True, blank=True, choices=grados)
    rut = models.CharField('rut', max_length=12, null=False, blank=False)
    nombres = models.CharField('nombres', max_length=200, null=False, blank=False)
    apellidos = models.CharField('apellidos', max_length=200, null=False, blank=False)
    edad = models.IntegerField('edad', null=False, blank=False)
    sexos = [("1", "Masculino"), ("2", "Femenino"), ]
    sexo = models.CharField(max_length=100, null=True, blank=True, choices=sexos)
    nacionalidad = models.CharField('nacionalidad', max_length=50, null=False, blank=False)
    ciudad_nacimiento = models.CharField(max_length=150, null=True)
    fecha_nacimiento = models.DateField()
    direccion = models.CharField(max_length=150, null=True, blank=True)
    estados = [("1", "Activo"), ("2", "Inactivo"), ]
    estado = models.CharField(max_length=100, null=True, blank=True, choices=estados)

    class Meta:
        verbose_name = 'Paciente'
        verbose_name_plural = 'Pacientes'

    def __str__(self):
        return self.nombres + " " + self.apellidos


class Ficha(models.Model):
    id = models.AutoField(primary_key=True)
    rut = models.CharField('rut paciente', max_length=12, null=False, blank=False)
    nombres = models.CharField('nombre paciente', max_length=200, null=False, blank=False)
    apellidos = models.CharField('apellido paciente', max_length=200, null=False, blank=False)
    representante = models.ForeignKey('gestion_representantes.Representante', on_delete=models.CASCADE)
    especialidad = models.ForeignKey('gestion_profesionales.Profesionale', on_delete=models.CASCADE)
    hora_atencion = models.TimeField(null=True, blank=True)
    fecha_atencion = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name = 'Ficha'
        verbose_name_plural = 'Fichas'

    def __str__(self):
        return self.nombres + " " + self.apellidos
