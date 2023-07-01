from django.db import models
from Web.utils import SOCIALS, BaseModel, ImageModel, VideoModel


# Create your models here.
class ContactHelp(BaseModel):
    number = models.CharField(max_length=200)

    def __str__(self):
        return self.number

    class Meta:
        db_table = "contact_help"
        verbose_name_plural = "Les Supports d'Aide client (Contact)"


class Social(BaseModel):
    network_name = models.CharField(max_length=200)
    social_type = models.CharField(max_length=25, choices=SOCIALS)
    url = models.URLField()

    def __str__(self):
        return self.network_name

    class Meta:
        db_table = "social"
        verbose_name_plural = 'Les Réseaux Sociaux AHSM'


class ContactUs(BaseModel):
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    subject = models.CharField(max_length=150)
    message = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = "contact_us"
        verbose_name_plural = 'Les Posts Clients pour AHSM'


class ContactClient(BaseModel):
    email = models.EmailField(max_length=250, blank=True)
    phone = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return self.email

    class Meta:
        db_table = "contact_client"
        verbose_name_plural = 'Les Contacts des temoignants Clients'
