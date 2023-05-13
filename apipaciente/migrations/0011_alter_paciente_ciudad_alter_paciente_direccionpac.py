# Generated by Django 4.1.7 on 2023-05-13 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apipaciente', '0010_alter_paciente_ciudad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='ciudad',
            field=models.CharField(choices=[['BogotÃ¡', 'MedellÃ\xadn'], ['Cali', 'Barranquilla'], ['Cartagena', 'CÃºcuta'], ['Bucaramanga', 'Pereira'], ['Santa Marta', 'IbaguÃ©'], ['Villavicencio', 'Valledupar'], ['Manizales', 'Pasto'], ['Armenia', 'MonterÃ\xada'], ['Neiva', 'PopayÃ¡n'], ['Sincelejo', 'Riohacha'], ['Tunja', 'QuibdÃ³'], ['Florencia', 'Yopal'], ['Mocoa', 'San AndrÃ©s']], max_length=255),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='direccionPac',
            field=models.CharField(max_length=40),
        ),
    ]
