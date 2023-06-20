from django.db import models
from django.utils.safestring import mark_safe
from Web.utils import BaseModel, STATES


# Create your models here.
class Address(BaseModel):
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    lot = models.CharField(max_length=100)
    state = models.CharField(max_length=100, choices=STATES)
    zip_code = models.CharField(verbose_name='Postal Code', max_length=10)
    map = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = 'Les Adrèsses'

    def __str__(self):
        return self.street

    def admin_map(self):
        return mark_safe(f"{self.map}")
