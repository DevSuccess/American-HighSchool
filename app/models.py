from django.core.validators import FileExtensionValidator
from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.utils.safestring import mark_safe
from django.core.validators import MaxValueValidator, MinValueValidator
from .constants import ACADEMICS, DAYS, CONTACTS, STATES, SOCIALS, upload_path


class BaseModel(models.Model):
    active = models.BooleanField(default=True, null=True)
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
        default='',
        null=True,
        blank=True
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
        ], default='', null=True, blank=True)

    def admin_video(self):
        if self.video:
            return mark_safe(f"<video width='150' controls ><source  type='video/mp4' src='{self.video.url}'></video>")
        else:
            return ""

    class Meta:
        abstract = True


class AboutList(models.Model):
    name = models.CharField(max_length=150)
    status = models.BooleanField(default=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'A Propos : Listes'


class About(BaseModel, ImageModel):
    title = models.CharField(max_length=150)
    key = models.CharField(max_length=100)
    libel = models.CharField(max_length=250)
    lists = models.ManyToManyField(AboutList)
    content = models.TextField(null=True)

    class Meta:
        verbose_name_plural = 'A Propos'

    def __str__(self):
        return self.title


class Activity(BaseModel, ImageModel):
    title = models.CharField(max_length=150, null=True)

    class Meta:
        verbose_name_plural = 'Activités'

    def __str__(self):
        return self.title


class Address(BaseModel):
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    lot = models.CharField(max_length=100)
    state = models.CharField(max_length=100, choices=STATES)
    zip_code = models.CharField(verbose_name='Postal Code', max_length=10)
    map = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Adresses'

    def __str__(self):
        return self.street

    def admin_map(self):
        return mark_safe(f"{self.map}")


class Collaborator(BaseModel, ImageModel):
    name = models.CharField(max_length=150)
    date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Collaborateur'


class Accreditation(BaseModel, ImageModel):
    content = models.CharField(max_length=150)
    collaborators = models.ManyToManyField(Collaborator)

    def __str__(self):
        return self.content

    class Meta:
        verbose_name_plural = 'Accreditation'


class Contact(BaseModel):
    contact = models.CharField(max_length=200)
    type = models.CharField(max_length=50, choices=CONTACTS)

    def __str__(self):
        return self.contact

    class Meta:
        verbose_name_plural = 'Contacts'


class Hour(models.Model):
    day = models.CharField(max_length=5, choices=DAYS)
    open = models.TimeField()
    close = models.TimeField()
    active = models.BooleanField(default=True, null=True)
    message = models.CharField(max_length=250, default='')

    def clean(self):
        if self.open == self.close:
            raise ValidationError('Values must be different')

    class Meta:
        verbose_name_plural = 'Horaires'

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
    occupation = models.CharField(max_length=100)
    email = models.EmailField(max_length=250, unique=True)
    contacts = models.ManyToManyField(Contact)

    def __str__(self):
        return self.lastname

    class Meta:
        verbose_name_plural = 'Membres'


class Possibility(BaseModel):
    value = models.CharField(max_length=150)

    def __str__(self):
        return self.value

    class Meta:
        verbose_name_plural = 'Possibilités'


class Price(BaseModel, ImageModel):
    academic = models.CharField(max_length=10, choices=ACADEMICS, unique=True)
    price = models.FloatField()
    registration = models.FloatField()
    promotion = models.IntegerField(
        validators=[
            MaxValueValidator(100),
            MinValueValidator(1)
        ]
    )
    birth = models.IntegerField(
        validators=[
            MaxValueValidator(70),
            MinValueValidator(2)
        ],
        choices=[(i, str(i)) for i in range(72)]
    )
    possibilities = models.ForeignKey(Possibility, on_delete=models.CASCADE)

    def __str__(self):
        return self.academic

    class Meta:
        verbose_name_plural = 'Prix'


class Query(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    subject = models.CharField(max_length=150)
    message = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Démandes'


class ServiceType(BaseModel, ImageModel):
    name = models.CharField(max_length=150, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Service(BaseModel):
    title = models.CharField(max_length=150, null=True)
    key = models.CharField(max_length=150, null=True, blank=True)
    label = models.CharField(max_length=150, unique=True)
    info_line = models.CharField(max_length=15, null=True)
    all_service = models.ManyToManyField(ServiceType, verbose_name='Tout les Services', null=True)

    def __str__(self):
        return self.label


class Social(BaseModel):
    network_name = models.CharField(max_length=200)
    social_type = models.CharField(max_length=25, choices=SOCIALS)
    url = models.URLField()

    def __str__(self):
        return self.network_name

    class Meta:
        verbose_name_plural = 'Réseau Sociaux'


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
        verbose_name_plural = 'Témoignages'


class Value(BaseModel, ImageModel):
    content = models.TextField()


class Vision(BaseModel, ImageModel):
    title = models.CharField(max_length=150, blank=True)
    content = models.TextField()

    class Meta:
        verbose_name_plural = 'Visions'


class PresentationVideo(BaseModel, VideoModel):
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True)


class PresentationImage(BaseModel, ImageModel):
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True)
