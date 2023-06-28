from django.core.exceptions import ValidationError
from django.db import models
from datetime import timedelta
from django.utils import timezone


def validate_future_date(value):
    if value < timezone.now().date():
        raise ValidationError("La fecha debe ser válida.")

class Agendar(models.Model):
    IdCita = models.AutoField(primary_key=True, default=None)
    IdEspecialista = models.CharField(max_length=90)
    IdMedico = models.CharField(max_length=90)
    Fecha = models.DateField()
    Motivo = models.TextField()
    Hora = models.TimeField()
    Tipodeconsulta = models.CharField(max_length=80)
    Estados = models.CharField(max_length=80)
    IdPaciente = models.CharField(max_length=80)

    def clean(self):
        super().clean()

        try:
            validate_hour_separation(self.Fecha, self.Hora)
        except ValidationError as e:
            error_message = {'__all__': [str(e)]}
            raise ValidationError(error_message)

    def save(self, *args, **kwargs):
        self.full_clean()  # Realiza todas las validaciones
        super().save(*args, **kwargs)


def validate_hour_separation(fecha, hora):
    hora_actual = timezone.datetime.combine(fecha, hora)
    hora_anterior = hora_actual - timedelta(hours=1)
    hora_siguiente = hora_actual + timedelta(hours=1)

    citas_previas = Agendar.objects.filter(Fecha=fecha, Hora__gte=hora_anterior, Hora__lt=hora_actual)
    citas_posteriores = Agendar.objects.filter(Fecha=fecha, Hora__gt=hora_actual, Hora__lt=hora_siguiente)

    if citas_previas.exists() or citas_posteriores.exists():
        raise ValidationError('No se puede agendar una cita en este horario. Debe haber una separación de una hora entre citas.')
