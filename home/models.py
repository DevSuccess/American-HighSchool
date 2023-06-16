from django.db import models
from django.core.validators import FileExtensionValidator
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
    url = models.URLField()
    active = models.BooleanField(default=True)
    description = models.TextField(default='')
    file = models.FileField(
        upload_to=video_upload_path,
        validators=[
            FileExtensionValidator(allowed_extensions=['mp4'])
        ])

    def __str__(self):
        return self.title

    def admin_video(self):
        return mark_safe('<a href="{}"><img src="{}" width="70"/></a>'.format(self.file.url, self.file.url))
