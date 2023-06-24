from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError

from Web.utils import DAYS


# Create your models here.
class Hour(models.Model):
    day = models.CharField(max_length=15, choices=DAYS)
    open = models.TimeField()
    close = models.TimeField()
    message = models.CharField(max_length=250, blank=True)

    def clean(self):
        if self.open == self.close:
            raise ValidationError('Values must be different')

    class Meta:
        verbose_name_plural = "Les Horaires de AHSM"

    def __str__(self):
        return self.day

    @classmethod
    def get_current_hours(cls):
        now = timezone.now()
        current_day = now.strftime('%a')
        current_time = now.time()

        try:
            hour = cls.objects.get(day=current_day, open__lte=current_time, close__gt=current_time)
            return f"{hour.day}: {hour.open.strftime('%I:%M %p')} - {hour.close.strftime('%I:%M %p')}"
        except cls.DoesNotExist:
            return 'Closed'
