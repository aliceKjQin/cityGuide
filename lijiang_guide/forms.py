from django import forms
from .models import TrailReview

class TrailReviewForm(forms.ModelForm):
    class Meta:
        model = TrailReview
        fields = ['review', 'rating']
        