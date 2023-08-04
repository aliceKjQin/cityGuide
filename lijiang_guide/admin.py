from django.contrib import admin

# Register your models here.
from .models import Hiking, Cafe

admin.site.register(Hiking)
admin.site.register(Cafe)