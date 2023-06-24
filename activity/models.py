from django.db import models

from Web.utils import BaseModel, ImageModel


# Create your models here.
class Activity(BaseModel, ImageModel):
    title = models.CharField(max_length=150)
    description = models.TextField(max_length=500, null=True)

    class Meta:
        verbose_name_plural = 'Les Activités extra-scolaires'

    def __str__(self):
        return self.title
