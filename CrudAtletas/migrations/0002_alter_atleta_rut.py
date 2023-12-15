# Generated by Django 5.0 on 2023-12-14 16:33

import CrudAtletas.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CrudAtletas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atleta',
            name='rut',
            field=models.CharField(max_length=11, unique=True, validators=[CrudAtletas.models.validate_rut]),
        ),
    ]
