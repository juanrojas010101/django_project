# Generated by Django 4.1.7 on 2023-05-04 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apipaciente', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='telefonoPac',
            field=models.CharField(max_length=10),
        ),
    ]