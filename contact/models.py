from django.db import models
from Web.utils import SOCIALS, BaseModel, ImageModel, VideoModel


# Create your models here.
class Contact(models.Model):
    number = models.CharField(max_length=200)

    def __str__(self):
        return self.number

    class Meta:
        verbose_name_plural = "Les Contacts de AHS"


class Social(models.Model):
    network_name = models.CharField(max_length=200)
    social_type = models.CharField(max_length=25, choices=SOCIALS)
    url = models.URLField()

    def __str__(self):
        return self.network_name

    class Meta:
        db_table = "social"
        verbose_name_plural = 'Les Réseaux Sociaux de AHS'


class ContactUs(BaseModel):
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    subject = models.CharField(max_length=150)
    message = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = "contact_us"
        verbose_name_plural = 'Les Posts Clients pour AHS'