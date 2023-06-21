from django.db import models
from Web.utils import BaseModel, ImageModel


# Create your models here.
class Service(BaseModel, ImageModel):
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Les Services proposés par AHSM'
