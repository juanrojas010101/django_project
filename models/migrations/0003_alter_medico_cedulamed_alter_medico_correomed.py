# Generated by Django 4.1.7 on 2023-06-21 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0002_medico_activo_medico_fechasdisponibilidad_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medico',
            name='cedulaMed',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='medico',
            name='correoMed',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]
