from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from Web.utils import BaseModel, ImageModel


# Create your models here.
class Level(BaseModel):
    name = models.CharField(max_length=150)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "level"
        verbose_name_plural = "Les Niveaux d'Etude existant a l'AHSM"


class Price(BaseModel, ImageModel):
    value = models.DecimalField(max_digits=10, decimal_places=2)
    promotion = models.DecimalField(
        validators=[
            MaxValueValidator(100),
            MinValueValidator(0)
        ], blank=True, max_digits=10, decimal_places=2
    )
    price_promo = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    registration = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    birth = models.IntegerField(
        validators=[
            MaxValueValidator(70),
            MinValueValidator(2)
        ],
        choices=[(i, str(i)) for i in range(72)]
    )
    levels = models.OneToOneField(Level, on_delete=models.CASCADE, null=True)

    def formatted_price(self):
        return "{:,.0f} MGA".format(self.price_promo)

    def formatted_registration(self):
        return "{:,.0f} MGA".format(self.registration)

    def calculate_price_promo(self):
        if self.promotion is not None:
            self.price_promo = self.value * (1 - self.promotion / 100)
        else:
            self.price_promo = self.value

    def save(self, *args, **kwargs):
        self.calculate_price_promo()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.value}"

    class Meta:
        db_table = "price"
        verbose_name_plural = 'Les Prix de formation ASHM'
