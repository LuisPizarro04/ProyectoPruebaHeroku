# Generated by Django 3.0.8 on 2021-07-12 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Representante',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('rut', models.CharField(max_length=12, verbose_name='rut')),
                ('nombres', models.CharField(max_length=200, verbose_name='nombres')),
                ('apellidos', models.CharField(max_length=200, verbose_name='apellidos')),
                ('edad', models.IntegerField(verbose_name='edad')),
                ('sexo', models.CharField(blank=True, choices=[('1', 'Masculino'), ('2', 'Femenino')], max_length=100, null=True)),
                ('nacionalidad', models.CharField(max_length=50, verbose_name='nacionalidad')),
                ('ciudad_nacimiento', models.CharField(max_length=150, null=True)),
                ('fecha_nacimiento', models.DateField()),
                ('direccion', models.CharField(blank=True, max_length=150, null=True)),
                ('contacto', models.CharField(max_length=12, verbose_name='contacto')),
                ('correo', models.EmailField(max_length=254, verbose_name='correo electronico')),
                ('estado', models.CharField(blank=True, choices=[('1', 'Activo'), ('2', 'Inactivo')], max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'Apoderado',
                'verbose_name_plural': 'Apoderados',
            },
        ),
    ]
