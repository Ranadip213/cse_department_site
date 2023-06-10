from django.db import models

# Create your models here.


class Gallery(models.Model):
    topic = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.ImageField(blank=True, null=True)
    image = models.ImageField(upload_to='upload/', blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('date_added',)

    def __str__(self):
        return self.topic
    
    def get_absolute_url(self):
        return f'/{self.slug}/'
    
    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:5500/' +self.image.url
        return ''

class Club(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='club_images/')
    url = models.URLField()

    def __str__(self):
        return self.name