from django.db import models
from datetime import datetime

# Create your models here.
class Post(models.Model):  # Use capitalized class name by convention
    title = models.CharField(max_length=120)
    description = models.CharField(max_length=500)  # Added max_length
    author = models.CharField(max_length=50)
    created_at = models.DateTimeField(default=datetime.now, blank=True)  # Use DateTimeField for timestamp
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title
class meta:
    verbose_name='post'
    verbose_name_plural='posts'