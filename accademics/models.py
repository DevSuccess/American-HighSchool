from django.db import models

from Web.utils import BaseModel, ImageModel


# Create your models here.
class Academic(BaseModel, ImageModel):
    name = models.CharField(max_length=150)
    description = models.TextField()

    class Meta:
        verbose_name_plural = "Les academies au sein de l'AHS"

    def __str__(self):
        return self.name
