# Generated by Django 4.1.7 on 2023-06-28 03:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('agendar', '0005_alter_agendar_fecha'),
    ]

    operations = [
        migrations.AddField(
            model_name='agendar',
            name='IdPaciente',
            field=models.CharField(default=django.utils.timezone.now, max_length=80),
            preserve_default=False,
        ),
    ]
