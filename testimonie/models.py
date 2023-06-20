from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from Web.utils import BaseModel, ImageModel


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

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Les Témoignages'
