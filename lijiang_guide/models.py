from django.db import models
from django.contrib.auth.models import User

class Hiking(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    google_map = models.URLField()
    hiking_image = models.ImageField(null=True, blank=True, upload_to='hiking_images/')
    description = models.TextField(null=True)

    def __str__(self):
        return self.name
    

class TrailReview(models.Model):
    RATING = [
        (1, 'One Star' ),
        (2, 'Two Stars'),
        (3, 'Three Stars'),
        (4, 'Four Stars'),
        (5, 'Five Stars'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    trail = models.ForeignKey(Hiking, on_delete=models.CASCADE)
    review = models.TextField()
    star_rating = models.IntegerField(default=None)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Plural name for admin interface for model TrailReview
        verbose_name_plural = "Trail Reviews"

    def __str__(self):
        if len(self.review) > 50:
            result = f"{self.review[:50]}..."
        else:
            result = self.review

        return result

class Cafe(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    google_map = models.URLField()
    cafe_image = models.ImageField(null=True, blank=True, upload_to='cafe_images/')

    def __str__(self):
        return self.name
    

class Rental(models.Model):
    name = models.CharField(max_length=250)
    location = models.CharField(max_length=250)
    map = models.URLField()
    rental_main = models.ImageField(null=True, blank=True, upload_to='rental_images')
    living_room = models.ImageField(null=True, blank=True, upload_to='rental_images')
    bedroom = models.ImageField(null=True, blank=True, upload_to='rental_images')
    bathroom = models.ImageField(null=True, blank=True, upload_to='rental_images')

    def __str__(self):
        return self.name

