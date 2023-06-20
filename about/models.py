from django.db import models
from Web.utils import BaseModel, ImageModel, VideoModel


# Create your models here.
class About(BaseModel, ImageModel):
    title = models.CharField(max_length=150)
    key = models.CharField(max_length=100)
    libel = models.CharField(max_length=250)
    content = models.TextField()

    class Meta:
        verbose_name_plural = 'Les Propos'

    def __str__(self):
        return self.title


class Info(BaseModel):
    title = models.CharField(max_length=100)
    email = models.EmailField(max_length=150)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Les Informations lier à AHSM'
