from django.db import models

class Notice(models.Model):
    topic = models.CharField(max_length=255)
    Slug = models.SlugField()
    description = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

class Events(models.Model):
    topic = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)