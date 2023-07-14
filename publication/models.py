from django.db import models
from django.contrib.auth.models import User

from Web.utils import ImageModel, BaseModel

# Create your models here.
STATUS = (
    (0, "Draft"),  # Brouillons
    (1, "Publish")  # Article
)


class Author(ImageModel):
    name = models.CharField(max_length=200, unique=True)

    class Meta:
        verbose_name_plural = "Les Managers"

    def __str__(self):
        return self.name


class Post(BaseModel, ImageModel):
    title = models.CharField(max_length=200, unique=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    content = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        verbose_name_plural = "Les News et Publications"
        ordering = ['-created_at']

    def __str__(self):
        return self.title
