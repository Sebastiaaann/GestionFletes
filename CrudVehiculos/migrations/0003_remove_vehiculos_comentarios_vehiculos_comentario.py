# Generated by Django 4.2.6 on 2023-12-01 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CrudVehiculos', '0002_alter_vehiculos_estado'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehiculos',
            name='comentarios',
        ),
        migrations.AddField(
            model_name='vehiculos',
            name='comentario',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
    ]
