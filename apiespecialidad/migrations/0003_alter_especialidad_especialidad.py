# Generated by Django 4.1.7 on 2023-05-16 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiespecialidad', '0002_alter_especialidad_especialidad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='especialidad',
            name='especialidad',
            field=models.CharField(choices=[['AnestesiologÃ\xada', 'AnestesiologÃ\xada'], ['CardiologÃ\xada', 'CardiologÃ\xada'], ['DermatologÃ\xada', 'DermatologÃ\xada'], ['EndocrinologÃ\xada', 'EndocrinologÃ\xada'], ['GastroenterologÃ\xada', 'GastroenterologÃ\xada'], ['GeriatrÃ\xada', 'GeriatrÃ\xada'], ['GinecologÃ\xada', 'GinecologÃ\xada'], ['HematologÃ\xada', 'HematologÃ\xada'], ['InfectologÃ\xada', 'InfectologÃ\xada'], ['Medicina del deporte', 'Medicina del deporte'], ['Medicina familiar y comunitaria', 'Medicina familiar y comunitaria'], ['Medicina interna', 'Medicina interna'], ['NefrologÃ\xada', 'NefrologÃ\xada'], ['NeurologÃ\xada', 'NeurologÃ\xada'], ['Obstetricia', 'Obstetricia'], ['OncologÃ\xada', 'OncologÃ\xada'], ['OftalmologÃ\xada', 'OftalmologÃ\xada'], ['Ortopedia', 'Ortopedia'], ['OtorrinolaringologÃ\xada', 'OtorrinolaringologÃ\xada'], ['PediatrÃ\xada', 'PediatrÃ\xada'], ['PsiquiatrÃ\xada', 'PsiquiatrÃ\xada'], ['RadiologÃ\xada', 'RadiologÃ\xada'], ['ReumatologÃ\xada', 'ReumatologÃ\xada'], ['Salud pÃºblica', 'Salud pÃºblica'], ['UrologÃ\xada', 'UrologÃ\xada']], max_length=35),
        ),
    ]
