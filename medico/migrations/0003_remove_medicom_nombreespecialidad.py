# Generated by Django 4.1.7 on 2023-06-23 17:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medico', '0002_rename_idespecialidad_medicom_nombreespecialidad'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medicom',
            name='NombreEspecialidad',
        ),
    ]