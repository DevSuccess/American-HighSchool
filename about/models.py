from django.db import models
from Web.utils import ImageModel
from contact.models import Contact


# Create your models here.
class Support(models.Model):
    title = models.CharField(max_length=100)
    email = models.EmailField(max_length=150)
    contacts = models.ManyToManyField(Contact)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Le Support AHS"


class Info(ImageModel):
    title = models.CharField(max_length=150)
    description = models.TextField()

    class Meta:
        verbose_name_plural = 'Les Missions, Visions et Organisations'

    def __str__(self):
        return f"{self.title}"
