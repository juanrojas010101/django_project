# Generated by Django 4.1.7 on 2023-06-21 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('idMedico', models.AutoField(primary_key=True, serialize=False)),
                ('NombreCompletoMed', models.CharField(max_length=90)),
                ('NumeroTarjetaMed', models.CharField(max_length=50)),
                ('cedulaMed', models.IntegerField(null=True)),
                ('telefonoMed', models.CharField(max_length=10)),
                ('correoMed', models.EmailField(max_length=254, null=True)),
                ('ciudadMed', models.CharField(max_length=90)),
                ('especialidad', models.CharField(max_length=50)),
                ('direccionConsultorio', models.CharField(max_length=50)),
                ('IdEspecialidad', models.CharField(max_length=80)),
                ('IdCiudad', models.CharField(max_length=90)),
            ],
        ),
    ]
