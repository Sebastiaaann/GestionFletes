# Generated by Django 4.2.6 on 2023-11-29 20:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('CrudVehiculos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mantenciones',
            fields=[
                ('codigo', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('fecha', models.DateField()),
                ('valor', models.PositiveIntegerField()),
                ('vehiculo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CrudVehiculos.vehiculos')),
            ],
        ),
    ]
