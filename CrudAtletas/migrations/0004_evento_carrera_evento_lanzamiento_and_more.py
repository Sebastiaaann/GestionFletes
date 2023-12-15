# Generated by Django 5.0 on 2023-12-14 17:51

import CrudAtletas.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CrudAtletas', '0003_alter_atleta_rut'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='carrera',
            field=models.CharField(blank=True, choices=[('1', '100 metros'), ('2', 'Maraton')], max_length=50),
        ),
        migrations.AddField(
            model_name='evento',
            name='lanzamiento',
            field=models.CharField(blank=True, choices=[('1', 'Lanzamiento de peso'), ('2', 'Lanzamiento de disco'), ('3', 'Lanzamiento de martillo'), ('4', 'Lanzamiento de jabalina')], max_length=50),
        ),
        migrations.AddField(
            model_name='evento',
            name='prueba_combinada',
            field=models.CharField(blank=True, choices=[('Masculino', 'Decatlón'), ('Femenino', 'Heptatlón')], max_length=50),
        ),
        migrations.AddField(
            model_name='evento',
            name='salto',
            field=models.CharField(blank=True, choices=[('1', 'Salto de altura'), ('2', 'Salto de longitud'), ('3', 'Salto con pértiga')], max_length=50),
        ),
        migrations.AlterField(
            model_name='atleta',
            name='rut',
            field=models.CharField(error_messages={'unique': ' Ya existe un Usuario con este RUt.'}, max_length=12, unique=True, validators=[CrudAtletas.models.validate_rut]),
        ),
    ]
