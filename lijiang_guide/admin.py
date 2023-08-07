from django.contrib import admin

# Register your models here.
from .models import Hiking, Cafe, TrailReview

admin.site.register(Hiking)
admin.site.register(Cafe)
admin.site.register(TrailReview)