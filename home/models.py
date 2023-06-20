from django.db import models
from Web.utils import DAYS, BaseModel, ImageModel, VideoModel


class Activity(BaseModel, ImageModel):
    title = models.CharField(max_length=150)

    class Meta:
        verbose_name_plural = 'Les Activités'

    def __str__(self):
        return self.title


class Possibility(BaseModel):
    value = models.CharField(max_length=150)

    def __str__(self):
        return self.value

    class Meta:
        verbose_name_plural = 'Les Possibilités'


class PresentationVideo(BaseModel, VideoModel):
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'La Présentation Vidéo'


class PresentationImage(BaseModel, ImageModel):
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'La Présentation Photo'
