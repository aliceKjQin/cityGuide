from django.shortcuts import render
from .models import Hiking, Cafe
from .forms import TrailReviewForm

def index(request):
    return render(request, 'lijiang_guide/index.html')

def hiking(request):
    trails = Hiking.objects.all()
    return render(request, 'lijiang_guide/hiking.html', {
        'trails': trails,
    })

def Trail(request, trail_id):
    trail = Hiking.objects.get(id=trail_id)
    
    if request.method != 'POST':
        form = TrailReviewForm
    else:
        form = TrailReviewForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'lijiang_guide/trail.html', {
        'trail': trail,
        'form': form,
    })

def cafe(request):
    cafes = Cafe.objects.all()
    return render(request, 'lijiang_guide/cafe.html', {
        'cafes': cafes,
    })

