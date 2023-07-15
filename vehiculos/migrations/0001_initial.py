# Generated by Django 3.2.13 on 2023-07-03 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=100)),
                ('modelo', models.CharField(max_length=100)),
                ('serial_carroceria', models.CharField(max_length=100)),
                ('serial_motor', models.CharField(max_length=100)),
                ('categoria', models.CharField(max_length=100)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=7)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('last_edit', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
