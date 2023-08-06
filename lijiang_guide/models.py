from django.db import models
from django.contrib.auth.models import User

class Hiking(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    google_map = models.URLField()
    hiking_image = models.ImageField(null=True, blank=True, upload_to='hiking_images/')

    def __str__(self):
        return self.name
    

class TrailReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    trail = models.ForeignKey(Hiking, on_delete=models.CASCADE)
    review = models.TextField()
    rating = models.IntegerField(choices=RATING, default=None)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Trail Reviews"

    def __str__(self):
        return self.trail
    
    def get_rating(self):
        return self.rating

class Cafe(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    google_map = models.URLField()
    cafe_image = models.ImageField(null=True, blank=True, upload_to='cafe_images/')

    def __str__(self):
        return self.name

