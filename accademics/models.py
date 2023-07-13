from django.db import models

from Web.utils import BaseModel, ImageModel

TYPES = (
    ('A', 'A'),
    ('B', 'B'),
    ('C', 'C'),
    ('D', 'D')
)


# Create your models here.
class Accademics(BaseModel, ImageModel):
    name = models.CharField(max_length=150)
    type = models.CharField(max_length=1, choices=TYPES, null=True)
    description = models.TextField()

    class Meta:
        db_table = "accademic"
        verbose_name_plural = "Les accademies dans AHSM"
        ordering = ['type']

    def __str__(self):
        return self.name
