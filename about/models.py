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
    TYPES = (
        ('A', 'Mission'),
        ('B', 'Vision'),
        ('C', 'Programme')
    )
    title = models.CharField(max_length=150)
    libel = models.TextField(blank=True, null=True, default=' ')
    description = models.TextField()
    type = models.CharField(max_length=1, choices=TYPES)

    class Meta:
        verbose_name_plural = 'Les Missions, Visions et Organisations'

    def __str__(self):
        return f"{self.type} : {self.title}"
