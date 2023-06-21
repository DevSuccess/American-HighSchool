from django.db import models


class Registration(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    age = models.IntegerField()
    gender = models.CharField(max_length=10, choices=(('male', 'Male'), ('female', 'Female')))

    # Add any additional fields you want to store in the model

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
