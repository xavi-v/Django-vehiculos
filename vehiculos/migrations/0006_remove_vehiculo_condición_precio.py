# Generated by Django 3.2.13 on 2023-07-07 00:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculos', '0005_vehiculo_condición_precio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehiculo',
            name='condición_precio',
        ),
    ]
