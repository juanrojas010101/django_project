# Generated by Django 4.1.7 on 2023-06-02 00:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0004_medico_ciudadmed'),
    ]

    operations = [
        migrations.AddField(
            model_name='medico',
            name='IdEspecialidad',
            field=models.CharField(default=django.utils.timezone.now, max_length=80),
            preserve_default=False,
        ),
    ]
