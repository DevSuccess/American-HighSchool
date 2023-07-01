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
        db_table = "about_ahsm"
        verbose_name_plural = "Les Informations sur AHSH"

    def __str__(self):
        return self.title


class AboutHelp(BaseModel):
    title = models.CharField(max_length=100)
    email = models.EmailField(max_length=150)
    contacts = models.ManyToManyField(ContactHelp, related_name="about_to_contact")

    def __str__(self):
        return self.title

    class Meta:
        db_table = "about_help"
        verbose_name_plural = "Les Supports d'Aide Client (About) "


class AboutITTI(BaseModel):
    pass

    class Meta:
        db_table = "about_itti"
        verbose_name_plural = 'Les Informations sur ITTI'


class About(models.Model):
    TYPES = (
        ('A', 'Mission'),
        ('B', 'Vision')
    )
    title = models.CharField(max_length=150)
    libel = models.TextField(blank=True, null=True, default=' ')
    description = models.TextField()
    type = models.CharField(max_length=1, choices=TYPES)

    class Meta:
        db_table = "about_us"
        verbose_name_plural = 'Les Missions et Visions'

    def __str__(self):
        return f"{self.type} : {self.title}"
