# Generated by Django 4.1.7 on 2023-06-28 19:40

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('apiespecialidad', '0002_especialidad_guidespecialista'),
    ]

    operations = [
        migrations.AlterField(
            model_name='especialidad',
            name='guidEspecialista',
            field=models.UUIDField(default=uuid.uuid4),
        ),
    ]