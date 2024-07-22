from django.db import models
from django.utils import timezone
import datetime

# Create your models here.


class ContentGeneration(models.Model):
    id = models.AutoField(primary_key=True)
    datetime = models.DateTimeField(default=datetime.datetime.now)
    input_context = models.TextField()
    content_output = models.TextField()
    email = models.EmailField()

    def save(self, *args, **kwargs):
        if self.datetime and timezone.is_naive(self.datetime):
            self.datetime = timezone.make_aware(self.datetime, timezone.get_current_timezone())
        super().save(*args, **kwargs)

    def __str__(self):
        return f"ContentGeneration(id={self.id}, email={self.email})"
