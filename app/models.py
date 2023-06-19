from django.core.validators import FileExtensionValidator
from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.utils.safestring import mark_safe
from django.core.validators import MaxValueValidator, MinValueValidator
from .constants import DAYS, STATES, SOCIALS, upload_path, CATEGORY


class BaseModel(models.Model):
    active = models.BooleanField(default=True,)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class ImageModel(models.Model):
    image = models.FileField(
        upload_to=upload_path,
        validators=[
            FileExtensionValidator(allowed_extensions=['png', 'jpg', 'gif', 'jpeg', 'webp', 'svg', 'bmp'])
        ],
        default=''
    )

    def admin_photo(self):
        if self.image:
            return mark_safe(f"<a href='{self.image.url}'><img src='{self.image.url}' width='100' /></a>")
        else:
            return ""

    class Meta:
        abstract = True


class VideoModel(models.Model):
    video = models.FileField(
        upload_to=upload_path,
        validators=[
            FileExtensionValidator(allowed_extensions=['mp4', 'avi', 'mov'])
        ], default='')

    def admin_video(self):
        if self.video:
            return mark_safe(f"<video width='150' controls ><source  type='video/mp4' src='{self.video.url}'></video>")
        else:
            return ""

    class Meta:
        abstract = True


class Price(BaseModel):
    price = models.FloatField()
    promotion = models.IntegerField(
        validators=[
            MaxValueValidator(100),
            MinValueValidator(0)
        ], blank=True
    )
    price_promo = models.FloatField(blank=True)
    registration = models.FloatField(blank=True)
    birth = models.IntegerField(
        validators=[
            MaxValueValidator(70),
            MinValueValidator(2)
        ],
        choices=[(i, str(i)) for i in range(72)]
    )

    def calculate_price_promo(self):
        if self.promotion is not None:
            self.price_promo = self.price * (1 - self.promotion / 100)
        else:
            self.price_promo = self.price

    def save(self, *args, **kwargs):
        self.calculate_price_promo()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.price

    class Meta:
        verbose_name_plural = 'Les Prix'


class Level(BaseModel, ImageModel):
    name = models.CharField(max_length=150)
    status = models.BooleanField(default=True)
    prices = models.ForeignKey(Price, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Les Niveaux'


class About(BaseModel, ImageModel):
    title = models.CharField(max_length=150)
    key = models.CharField(max_length=100)
    libel = models.CharField(max_length=250)
    content = models.TextField()

    class Meta:
        verbose_name_plural = 'Les Propos'

    def __str__(self):
        return self.title


class Activity(BaseModel, ImageModel):
    title = models.CharField(max_length=150)

    class Meta:
        verbose_name_plural = 'Les Activités'

    def __str__(self):
        return self.title


class Address(BaseModel):
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    lot = models.CharField(max_length=100)
    state = models.CharField(max_length=100, choices=STATES)
    zip_code = models.CharField(verbose_name='Postal Code', max_length=10)
    map = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = 'Les Adrèsses'

    def __str__(self):
        return self.street

    def admin_map(self):
        return mark_safe(f"{self.map}")


class Collaborator(BaseModel, ImageModel):
    name = models.CharField(max_length=150)
    date = models.DateField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Les Collaborateurs'


class Accreditation(BaseModel, ImageModel):
    content = models.CharField(max_length=150)

    def __str__(self):
        return self.content

    class Meta:
        verbose_name_plural = 'Les Accreditations'


class Contact(BaseModel):
    number = models.CharField(max_length=200)

    def __str__(self):
        return self.number

    class Meta:
        verbose_name_plural = 'Les Contacts'


class Social(BaseModel):
    network_name = models.CharField(max_length=200)
    social_type = models.CharField(max_length=25, choices=SOCIALS)
    url = models.URLField()

    def __str__(self):
        return self.network_name

    class Meta:
        verbose_name_plural = 'Les Réseau Sociaux'


class Info(BaseModel):
    title = models.CharField(max_length=100)
    email = models.EmailField(max_length=150)
    phones = models.ManyToManyField(Contact)
    socials = models.ManyToManyField(Social)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Les Informations lier à AHSM'


class Hour(BaseModel):
    day = models.CharField(max_length=15, choices=DAYS)
    open = models.TimeField()
    close = models.TimeField()
    message = models.CharField(max_length=250, default='')

    def clean(self):
        if self.open == self.close:
            raise ValidationError('Values must be different')

    class Meta:
        verbose_name_plural = 'Les Horaires'

    def __str__(self):
        return self.day

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    @classmethod
    def get_current_hours(cls):
        now = timezone.now()
        current_day = now.strftime('%a')

        try:
            hour = cls.objects.get(day=current_day, active=True)
            return f"{hour.day}: {hour.open.strftime('%I.%M %p')} - {hour.close.strftime('%I.%M %p')}"
        except cls.DoesNotExist:
            return 'Closed'


class Members(BaseModel, ImageModel):
    lastname = models.CharField(max_length=100)
    firstname = models.CharField(max_length=150)
    category = models.CharField(max_length=2, choices=CATEGORY)
    occupation = models.CharField(max_length=100)
    email = models.EmailField(max_length=250, unique=True)
    contacts = models.ManyToManyField(Contact)

    def __str__(self):
        return self.lastname

    class Meta:
        verbose_name_plural = 'Les Membres'


class Possibility(BaseModel):
    value = models.CharField(max_length=150)

    def __str__(self):
        return self.value

    class Meta:
        verbose_name_plural = 'Les Possibilités'


class Query(BaseModel):
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    subject = models.CharField(max_length=150)
    message = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Les Démandes Utilisateurs'


class Service(BaseModel, ImageModel):
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Les Services'


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


class Vision(BaseModel, ImageModel):
    title = models.CharField(max_length=150, blank=True)
    content = models.TextField()

    class Meta:
        verbose_name_plural = 'Les Visions'

    def __str__(self):
        return self.title


class PresentationVideo(BaseModel, VideoModel):
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'La Présentation Vidéo'


class PresentationImage(BaseModel, ImageModel):
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'La Présentation Photo'
