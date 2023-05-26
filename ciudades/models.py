from django.db import models

# Create your models here.

class Ciudad(models.Model):
    id = models.IntegerField(primary_key=True)
    city = models.CharField(max_length=90)
