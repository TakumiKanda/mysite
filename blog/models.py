from django.db import models
from django.utils import timezone
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
import datetime


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
      
class Photo(models.Model):
    image = ProcessedImageField(upload_to='images',
                                processors=[ResizeToFill(int(175*2*1.414), 175*2)],
                                options={'quality': 100})
    color_tag = models.CharField(max_length = 100, default = "NULL")
    created_date = models.CharField(max_length = 100, default = "NULL")