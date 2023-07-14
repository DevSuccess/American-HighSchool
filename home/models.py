from django.db import models
from Web.utils import BaseModel, ImageModel, VideoModel


class PageGarde(BaseModel, ImageModel):
    title = models.CharField(max_length=150)
    libel = models.CharField(max_length=250)
    key = models.CharField(max_length=100)
    content = models.TextField()

    class Meta:
        verbose_name_plural = "Le Page de Garde"

    def __str__(self):
        return self.title


class PresentationVideo(BaseModel, VideoModel):
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "p_video"
        verbose_name_plural = 'Les Présentations Vidéo AHS'


class PresentationImage(BaseModel, ImageModel):
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "p_image"
        verbose_name_plural = 'Les Présentations Photo AHS'


class Activity(BaseModel, ImageModel):
    title = models.CharField(max_length=150)

    class Meta:
        db_table = "activity"
        verbose_name_plural = 'Les Activités Extra-scolaires'

    def __str__(self):
        return self.title


class Membership(BaseModel, ImageModel):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "L'Image des membres"
