# Generated by Django 4.1.7 on 2023-06-23 17:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medico', '0003_remove_medicom_nombreespecialidad'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medicom',
            name='IdCiudad',
        ),
    ]