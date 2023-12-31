# Generated by Django 4.2.6 on 2023-11-29 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehiculos',
            fields=[
                ('vehiculoID', models.AutoField(primary_key=True, serialize=False)),
                ('patente', models.CharField(max_length=6, unique=True)),
                ('marca', models.CharField(max_length=30)),
                ('modelo', models.CharField(max_length=50)),
                ('fechaAdquisicion', models.DateField()),
                ('estado', models.CharField(choices=[('activo', 'Activo'), ('inactivo', 'Inactivo')], default='activo', max_length=10)),
                ('comentarios', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
