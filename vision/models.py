from django.db import models

from Web.utils import BaseModel, ImageModel


# Create your models here.
class Vision(BaseModel, ImageModel):
    title = models.CharField(max_length=150, blank=True)
    content = models.TextField()

    class Meta:
        verbose_name_plural = 'Les Visions'

    def __str__(self):
        return self.title
