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
    RATING = [
        (1, 'One Star' ),
        (2, 'Two Stars'),
        (3, 'Three Stars'),
        (4, 'Four Stars'),
        (5, 'Five Stars'),
    ]

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    trail = models.ForeignKey(Hiking, on_delete=models.CASCADE)
    review = models.TextField()
    rating = models.IntegerField(choices=RATING, default=None)
    date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Trail Reviews"

    def __str__(self):
        if len(self.review) > 50:
            truncated_review = f"{self.review[:50]}..."
        else:
            truncated_review = self.review
        
        stars_html = ''.join(['<i class="fa-solid fa-star"></i>' for i in range(self.rating)])

        return f"{stars_html} {truncated_review}"

class Cafe(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    google_map = models.URLField()
    cafe_image = models.ImageField(null=True, blank=True, upload_to='cafe_images/')

    def __str__(self):
        return self.name

