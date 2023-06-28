# Generated by Django 4.1.7 on 2023-06-28 19:37

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('apiespecialidad', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='especialidad',
            name='guidEspecialista',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]
