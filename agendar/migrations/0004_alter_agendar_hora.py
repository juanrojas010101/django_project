# Generated by Django 4.1.7 on 2023-06-27 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agendar', '0003_alter_agendar_hora'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agendar',
            name='Hora',
            field=models.TimeField(),
        ),
    ]
