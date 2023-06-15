from django.db import models
from django.core.exceptions import ValidationError

DAYS = (
    ('Mon', 'Monday'),
    ('Tue', 'Tuesday'),
    ('Wed', 'Wednesday'),
    ('Thu', 'Thursday'),
    ('Fri', 'Friday'),
    ('Sat', 'Saturday'),
    ('Sun', 'Sunday'),
)

CONTACTS = (
    ('fa-envelope', 'Email'),
    ('fa-phone-alt', 'Phone'),
    ('fa-whatsapp', 'WhatsApp'),
)

SOCIALS = (
    ('fa-linkedin-in', 'LinkedIn'),
    ('fa-twitter', 'Twitter'),
    ('fa-facebook-f', 'Facebook'),
    ('fa-instagram', 'Instagram'),
)


# Create your models here.
class Contact(models.Model):
    contact = models.CharField(max_length=200)
    contact_type = models.CharField(max_length=25, choices=CONTACTS)
    active = models.BooleanField(default=True, null=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.contact


class Social(models.Model):
    network_name = models.CharField(max_length=200)
    social_type = models.CharField(max_length=25, choices=SOCIALS)
    url = models.URLField()
    active = models.BooleanField(default=True, null=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.network_name


class Information(models.Model):
    localisation = models.CharField(max_length=250)
    day_begin = models.CharField(max_length=3, choices=DAYS)
    day_end = models.CharField(max_length=3, choices=DAYS)
    time_begin = models.TimeField()
    time_end = models.TimeField()
    contacts = models.ManyToManyField(Contact)
    socials = models.ManyToManyField(Social)

    def __str__(self):
        return self.localisation

    def clean(self):
        if self.day_begin == self.day_end or self.time_begin == self.time_end:
            raise ValidationError('Values must be different')

        exist_records = Information.objects.count()
        if exist_records >= 1 and not self.pk:
            raise ValidationError('One values only')

    def save(self, *args, **kwargs):
        self.full_clean()  # Valider avant de sauvegarder
        super().save(*args, **kwargs)
