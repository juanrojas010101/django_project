# Generated by Django 4.1.7 on 2023-05-16 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apipaciente', '0008_delete_ciudad_paciente_ciudadpac'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='ciudadPac',
            field=models.CharField(choices=[['BogotÃ¡', 'MedellÃ\xadn'], ['Cali', 'Barranquilla'], ['Cartagena', 'CÃºcuta'], ['Bucaramanga', 'Pereira'], ['Santa Marta', 'IbaguÃ©'], ['Villavicencio', 'Valledupar'], ['Manizales', 'Pasto'], ['Armenia', 'MonterÃ\xada'], ['Neiva', 'PopayÃ¡n'], ['Sincelejo', 'Riohacha'], ['Tunja', 'QuibdÃ³'], ['Florencia', 'Yopal'], ['Mocoa', 'San AndrÃ©s']], max_length=100),
        ),
    ]
