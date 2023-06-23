from django.db import models
from django.contrib.auth.models import User

from Web.utils import ImageModel, BaseModel

STATUS = (
    (0, "Draft"),
    (1, "Publish")
)


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    image = models.ImageField(upload_to='blog/images/', blank=True, null=True)

    class Meta:
        verbose_name_plural = "Les Blogs"
        ordering = ['-created_on']

    def __str__(self):
        return self.title


class Slogan(BaseModel, ImageModel):
    title = models.CharField(max_length=200, unique=True)
    note = models.CharField(max_length=200, null=True)
    description = models.TextField()

    class Meta:
        verbose_name_plural = "Les Slogans"

    def __str__(self):
        return self.title
