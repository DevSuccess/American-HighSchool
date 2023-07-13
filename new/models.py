from django.db import models
from django.contrib.auth.models import User

# Create your models here.
STATUS = (
    (0, "Draft"),  # Brouillons
    (1, "Publish")  # Article
)


class UserPost(models.Model):
    image = models.ImageField(upload_to='news/images/users/')
    name = models.CharField(max_length=200, unique=True)

    class Meta:
        verbose_name_plural = "Les Utilisateurs"

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    author = models.ForeignKey(UserPost, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='news/images/posts/', blank=True, null=True)
    content = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "news"
        verbose_name_plural = "Les News"
        ordering = ['-created_on']

    def __str__(self):
        return self.title
