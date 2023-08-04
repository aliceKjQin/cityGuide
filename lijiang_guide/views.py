from django.shortcuts import render
from .models import Hiking, Cafe

def index(request):
    return render(request, 'lijiang_guide/index.html')

def hike(request):
    hikes = Hiking.objects.all()
    return render(request, 'lijiang_guide/hike.html', {
        'hikes': hikes,
    })

def cafe(request):
    cafes = Cafe.objects.all()
    return render(request, 'lijiang_guide/cafe.html', {
        'cafes': cafes,
    })