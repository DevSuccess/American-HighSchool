from django.db import models

from Web.utils import ImageModel, BaseModel

# Create your models here.
TYPES = (
    ('Abilitation', 'Abilitation'),
    ('Accreditation', 'Accreditation'),
    ('Homologation', 'Homologation'),
)


class List(BaseModel, ImageModel):
    name = models.CharField(max_length=150)
    type = models.CharField(max_length=25, choices=TYPES, null=True)
    date = models.DateField(null=True, blank=True, default='')
    description = models.TextField(null=True)

    class Meta:
        verbose_name_plural = "Les Lists des Merites"

    def __str__(self):
        return self.name


class Accreditation(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    lists = models.ManyToManyField(List)

    class Meta:
        db_table = "accreditation_value"
        verbose_name_plural = "Les Accreditations"

    def __str__(self):
        return self.title
