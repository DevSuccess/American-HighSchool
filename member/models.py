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
        db_table = "member"
        verbose_name_plural = "Les Membres constituant AHSM"
