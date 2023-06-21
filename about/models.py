from django.db import models
from Web.utils import BaseModel, ImageModel, VideoModel
from contact.models import ContactHelp


# Create your models here.
class AboutAHSM(BaseModel, ImageModel):
    title = models.CharField(max_length=150)
    key = models.CharField(max_length=100)
    libel = models.CharField(max_length=250)
    content = models.TextField()

    class Meta:
        verbose_name_plural = "Les Informations sur AHSH"

    def __str__(self):
        return self.title


class AboutHelp(BaseModel):
    title = models.CharField(max_length=100)
    email = models.EmailField(max_length=150)
    contacts = models.ManyToManyField(ContactHelp)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Les Supports d'Aide Client (About) "


class AboutITTI(BaseModel):
    pass
