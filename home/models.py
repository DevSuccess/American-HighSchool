from django.db import models
from Web.utils import BaseModel, ImageModel, VideoModel


class PresentationVideo(BaseModel, VideoModel):
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "p_video"
        verbose_name_plural = 'Les Présentations Vidéo AHSM'


class PresentationImage(BaseModel, ImageModel):
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "p_image"
        verbose_name_plural = 'Les Présentations Photo AHSM'


class Activity(BaseModel, ImageModel):
    title = models.CharField(max_length=150)
    description = models.TextField(max_length=500, null=True)

    class Meta:
        db_table = "activity"
        verbose_name_plural = 'Les Activités extra-scolaires'

    def __str__(self):
        return self.title
