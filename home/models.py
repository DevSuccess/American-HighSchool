from django.db import models
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError
from django.utils.safestring import mark_safe
import os


def video_upload_path(instance, filename):
    title = instance.title.replace("'", "")
    # Remplacer les espaces par des underscores et mettre tout en minuscule
    title = title.lower().replace(" ", "_")
    title = title.lower().replace(".", "_")

    # Retourner le chemin complet avec le nom du fichier
    return os.path.join("video", f"{title}_video", filename)


class Video(models.Model):
    title = models.CharField(max_length=250)
    url = models.URLField(default='', null=True, blank=True)
    active = models.BooleanField(default=True)
    description = models.TextField(default='', null=True, blank=True)
    file = models.FileField(
        upload_to=video_upload_path,
        validators=[
            FileExtensionValidator(allowed_extensions=['mp4'])
        ], default='', null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)

    def clean(self):
        # Vérifier que seul l'URL ou le fichier est rempli, pas les deux
        if self.url and self.file:
            raise ValidationError("You can only specify a URL or a video file, not both.")
        if not self.url and not self.file:
            raise ValidationError("Please specify a URL or video file.")

    def __str__(self):
        return self.title

    def admin_video(self):
        if self.url:
            return mark_safe(f"<a href='{self.url}'>Lien</a>")
        elif self.file:
            return mark_safe(f"<video width='150' controls ><source  type='video/mp4' src='{self.file.url}'></video>")

