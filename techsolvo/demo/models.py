from django.db import models

from datetime import datetime
from django.utils import timezone

from django.core.validators import FileExtensionValidator

# Create your models here.

class Song(models.Model):
    file = models.FileField(upload_to = 'audio',max_length=100,validators=[FileExtensionValidator(allowed_extensions=['mp3','wav','wma','amr'])])
    duration = models.PositiveIntegerField(blank=True, null=True)
    uploaded_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
    	return '{}'.format(self.file)



