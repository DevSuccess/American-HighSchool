from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from Web.utils import BaseModel, ImageModel


# Create your models here.
class Level(ImageModel):
    name = models.CharField(max_length=150)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Les Niveaux d'Etude existant à l'AHS"


class Price(BaseModel, ImageModel):
    value = models.DecimalField(max_digits=10, decimal_places=2)
    registration = models.DecimalField(max_digits=10, decimal_places=2)
    promotion = models.DecimalField(
        validators=[
            MaxValueValidator(100),
            MinValueValidator(0)
        ], blank=True, null=True, max_digits=10, decimal_places=2
    )
    birth = models.IntegerField(
        validators=[
            MaxValueValidator(70),
            MinValueValidator(2)
        ],
        choices=[(i, str(i)) for i in range(72)]
    )
    levels = models.ForeignKey(Level, on_delete=models.CASCADE, null=True)

    def formatted_registration(self):
        if self.registration is not None:
            return "{:,.0f} MGA".format(self.registration)
        else:
            return ""

    def formatted_value(self):
        if self.value is not None:
            return "{:,.0f} MGA".format(self.value)
        else:
            return ""

    def __str__(self):
        return f"{self.value}"

    class Meta:
        verbose_name_plural = 'Les Prix de formation AHS'
