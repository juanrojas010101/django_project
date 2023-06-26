from django.db import models

# Create your models here.

from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone

def validate_future_date(value):
    if value < timezone.now().date():
        raise ValidationError("La fecha debe ser valida.")

class Agendar(models.Model):
    IdEspecialista = models.CharField(max_length=90)
    IdMedico = models.CharField(max_length=90)
    Fecha = models.DateField(validators=[validate_future_date])
    Motivo = models.TextField()
    Hora = models.TimeField(unique_for_date='Fecha')
    Tipodeconsulta = models.CharField(max_length=80)
    Estados = models.CharField(max_length=30)
    
    # def clean(self):
    #     super().clean()
    #     if self.Fecha and self.Hora:
    #         start_time = timezone.datetime.combine(self.Fecha, self.Hora)
    #         end_time = start_time + timezone.timedelta(hours=1)
    #         overlapping_appointments = Agendar.objects.filter(
    #             Fecha=self.Fecha,
    #             Hora__range=[start_time.time(), end_time.time()]
    #         ).exclude(pk=self.pk)
    #         if overlapping_appointments.exists():
    #             raise ValidationError("Ya existe una cita programada en ese horario.")

    # def save(self, *args, **kwargs):
    #     self.clean()
    #     super().save(*args, **kwargs)