# Generated by Django 4.1.7 on 2023-06-16 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0008_alter_medico_direccionconsultorio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medico',
            name='direccionConsultorio',
            field=models.CharField(max_length=50),
        ),
    ]
