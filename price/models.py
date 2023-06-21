from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from Web.utils import BaseModel, ImageModel


# Create your models here.
class Price(BaseModel, ImageModel):
    price = models.DecimalField(max_digits=10, decimal_places=2)
    promotion = models.FloatField(
        validators=[
            MaxValueValidator(100),
            MinValueValidator(0)
        ], blank=True
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

    def formatted_price(self):
        return "{:,.0f} MGA".format(self.price)

    def formatted_registration(self):
        return "{:,.0f} MGA".format(self.registration)

    def calculate_price_promo(self):
        if self.promotion is not None:
            self.price_promo = self.price * (1 - self.promotion / 100)
        else:
            self.price_promo = self.price

    def save(self, *args, **kwargs):
        self.calculate_price_promo()
        super().save(*args, **kwargs)

    def __float__(self):
        return self.price

    class Meta:
        verbose_name_plural = 'Les Prix de formation ASHM'


class Level(BaseModel):
    name = models.CharField(max_length=150)
    status = models.BooleanField(default=True)
    prices = models.ForeignKey(Price, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Les Niveaux d'Etude existant a l'AHSM"
