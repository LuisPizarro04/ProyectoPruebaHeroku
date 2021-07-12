from django.db import models


class Representante(models.Model):
    id = models.AutoField(primary_key=True)
    rut = models.CharField('rut', max_length=12, null=False, blank=False)
    nombres = models.CharField('nombres', max_length=200, null=False, blank=False)
    apellidos = models.CharField('apellidos', max_length=200, null=False, blank=False)
    edad = models.IntegerField('edad', null=False, blank=False)
    sexos = [("1", "Masculino"), ("2", "Femenino"), ]
    sexo = models.CharField(max_length=100, null=True, blank=True, choices=sexos)
    nacionalidad = models.CharField('nacionalidad', max_length=50, null=False, blank=False)
    ciudad_nacimiento = models.CharField(max_length=150, null= True)
    fecha_nacimiento = models.DateField()
    direccion = models.CharField(max_length=150, null=True, blank=True)
    contacto = models.CharField('contacto', max_length=12, null=False, blank=False)
    correo = models.EmailField('correo electronico', blank=False, null=False)
    estados = [("1", "Activo"), ("2", "Inactivo"), ]
    estado = models.CharField(max_length=100, null=True, blank=True, choices=estados)

    class Meta:
        verbose_name = 'Apoderado'
        verbose_name_plural = 'Apoderados'

    def __str__(self):
        return self.nombres + " " + self.apellidos
