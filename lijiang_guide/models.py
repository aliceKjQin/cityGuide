from django.db import models

class Hiking(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    google_map = models.URLField()
    hiking_image = models.ImageField(null=True, blank=True, upload_to='hiking_images/')

    def __str__(self):
        return self.name

class Cafe(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    google_map = models.URLField()
    cafe_image = models.ImageField(null=True, blank=True, upload_to='cafe_images/')

    def __str__(self):
        return self.name

