from django.core.validators import FileExtensionValidator
from django.db import models
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
        return mark_safe(f"<a href='{self.image.url}'><img src='{self.image.url}' width='100' /></a>")

    class Meta:
        abstract = True


class VideoModel(models.Model):
    file = models.FileField(
        upload_to=upload_path,
        validators=[
            FileExtensionValidator(allowed_extensions=['mp4', 'avi', 'mov'])
        ], default='', null=True, blank=True)

    def admin_video(self):
        return mark_safe(f"<video width='150' controls ><source  type='video/mp4' src='{self.file.url}'></video>")

    class Meta:
        abstract = True


class Address(BaseModel):
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100, choices=STATES)
    url = models.TextField(null=True, blank=True)
    zip_code = models.CharField(max_length=10)

    def __str__(self):
        return self.street

    def admin_url(self):
        return mark_safe(f"{self.url}")


class AboutList(models.Model):
    title = models.CharField(max_length=150)
    status = models.BooleanField(default=True, null=True)

    def __str__(self):
        return self.title


class About(BaseModel, ImageModel):
    title = models.CharField(max_length=150)
    libel = models.CharField(max_length=250)
    lists = models.ForeignKey(AboutList, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title


class Activity(BaseModel, ImageModel):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Collaborator(BaseModel, ImageModel):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Accreditation(BaseModel, ImageModel):
    content = models.CharField(max_length=150)
    collaborators = models.ForeignKey(Collaborator, on_delete=models.CASCADE)

    def __str__(self):
        return self.content


class Contact(BaseModel):
    contact = models.CharField(max_length=200)
    contact_type = models.CharField(max_length=25, choices=CONTACTS)

    def __str__(self):
        return self.contact


class Hour(models.Model):
    day = models.CharField(max_length=5, choices=DAYS)
    open = models.TimeField()
    close = models.TimeField()
    active = models.BooleanField(default=True, null=True)
    message = models.CharField(max_length=250, default='')

    def clean(self):
        if self.open == self.close:
            raise ValidationError('Values must be different')

    def __str__(self):
        return self.day

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)


# class Information(models.Model):
#     name = models.CharField(max_length=150)
#     addresses = models.ForeignKey(Address, on_delete=models.CASCADE, null=True)
#     contacts = models.ForeignKey(Contact, on_delete=models.CASCADE, null=True)
#     hours = models.ForeignKey(Hour, on_delete=models.CASCADE)
#     socials = models.ForeignKey(Social, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.name
#
#     def clean(self):
#         exist_records = Information.objects.count()
#         if exist_records >= 1 and not self.pk:
#             raise ValidationError('One value only')
#
#     def save(self, *args, **kwargs):
#         self.full_clean()
#         super().save(*args, **kwargs)


class Members(BaseModel, ImageModel):
    lastname = models.CharField(max_length=100)
    firstname = models.CharField(max_length=150)
    occupation = models.CharField(max_length=100)
    email = models.EmailField(max_length=250, unique=True)
    contacts = models.ForeignKey(Contact, on_delete=models.CASCADE)

    def __str__(self):
        return self.lastname


class Possibility(BaseModel):
    value = models.CharField(max_length=150)

    def __str__(self):
        return self.value


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


class Service(BaseModel, ImageModel):
    label = models.CharField(max_length=150, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.label


class Social(BaseModel):
    network_name = models.CharField(max_length=200)
    social_type = models.CharField(max_length=25, choices=SOCIALS)
    url = models.URLField()

    def __str__(self):
        return self.network_name


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


class Value(BaseModel, ImageModel):
    content = models.TextField()


class Vision(BaseModel, ImageModel):
    title = models.CharField(max_length=150, blank=True)
    content = models.TextField()
