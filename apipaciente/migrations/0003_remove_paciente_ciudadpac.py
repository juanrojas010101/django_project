# Generated by Django 4.1.7 on 2023-05-26 01:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apipaciente', '0002_alter_paciente_ciudadpac_alter_paciente_idpaciente'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paciente',
            name='ciudadPac',
        ),
    ]
