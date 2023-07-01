from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from Web.utils import BaseModel, ImageModel

from contact.models import ContactClient


# Create your models here.
class Testimonial(BaseModel, ImageModel):
    name = models.CharField(max_length=250)
    content = models.TextField()
    start = models.IntegerField(
        validators=[
            MaxValueValidator(5),
            MinValueValidator(0)
        ],
        choices=[(i, str(i)) for i in range(6)]
    )
    occupation = models.CharField(max_length=150)
    contacts = models.ManyToManyField(ContactClient)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "testimonial"
        verbose_name_plural = 'Les Témoignages clients ou etudiant'
