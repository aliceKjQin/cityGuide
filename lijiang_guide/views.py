from django.shortcuts import render, redirect
from .models import Hiking, Cafe, TrailReview, Rental
from .forms import TrailReviewForm
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'lijiang_guide/index.html')

def hiking(request):
    trails = Hiking.objects.all()
    return render(request, 'lijiang_guide/hiking.html', {
        'trails': trails,
    })


def trail(request, trail_id):
    trail = Hiking.objects.get(id=trail_id)
    # Get the latest 5 reviews
    latest_reviews = TrailReview.objects.filter(trail=trail).order_by('-date')[:5]
    scale = TrailReview.rating_scale

    if request.method != 'POST':
        form = TrailReviewForm()
    else:
        form = TrailReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.trail = trail
            review.user = request.user
            review.save()
            return redirect('lijiang_guide:success_rating')

    return render(request, 'lijiang_guide/trail.html', {
        'trail': trail,
        'form': form,
        'latest_reviews': latest_reviews,
        'scale': scale,
    })

    

@login_required
def success_rating(request):
    return render(request, 'lijiang_guide/success_rating.html')

@login_required
def trail_reviews(request, trail_id):
    trail = Hiking.objects.get(id=trail_id)
    reviews = TrailReview.objects.filter(trail=trail).order_by('-date')
    
    return render(request, 'lijiang_guide/trail_reviews.html', {
        'trail': trail,
        'reviews': reviews,
    })


def cafe(request):
    cafes = Cafe.objects.all()
    return render(request, 'lijiang_guide/cafe.html', {
        'cafes': cafes,
    })

def rental(request):
    rentals = Rental.objects.all()
    return render(request, 'lijiang_guide/rental.html', {
        'rentals': rentals,
    })

def paypal_checkout(request):
    ...