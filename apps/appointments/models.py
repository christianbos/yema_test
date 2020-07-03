from django.db import models

from accounts.models import User, Pediatrician


class Appointment(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='appoinments',
    )
    pediatrician = models.ForeignKey(
        Pediatrician,
        on_delete=models.CASCADE,
        related_name='appoinments',
    )
    date = models.DateTimeField(
        blank=False,
        verbose_name='Dia y Hora'
    )
    comment = models.TextField(blank=False)

    class Meta:
        verbose_name = 'Cita'
        unique_together = ('user', 'pediatrician', 'date')
    def __str__(self):
        return f'Cita de {self.user} con el pediatra {self.pediatrician}'

