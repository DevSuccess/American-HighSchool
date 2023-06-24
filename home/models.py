from django.db import models
from Web.utils import BaseModel, ImageModel, VideoModel


class PresentationVideo(BaseModel, VideoModel):
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Les Présentations Vidéo AHSM'


class PresentationImage(BaseModel, ImageModel):
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Les Présentations Photo AHSM'
