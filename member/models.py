from django.db import models
from Web.utils import CATEGORY, BaseModel, ImageModel, VideoModel


# Create your models here.
class Member(BaseModel, ImageModel):
    lastname = models.CharField(max_length=100)
    firstname = models.CharField(max_length=150)
    category = models.CharField(max_length=2, choices=CATEGORY)
    occupation = models.CharField(max_length=100)

    def __str__(self):
        return self.lastname

    class Meta:
        verbose_name_plural = "Les Membres constituant AHSM"


class Collaborator(BaseModel, ImageModel):
    name = models.CharField(max_length=150)
    date = models.DateField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Les Collaborateurs de AHSM'


class Accreditation(BaseModel, ImageModel):
    content = models.CharField(max_length=150)

    def __str__(self):
        return self.content

    class Meta:
        verbose_name_plural = 'Les Accreditations de AHSM'

