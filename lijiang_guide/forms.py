from django import forms
from .models import TrailReview

class TrailReviewForm(forms.ModelForm):
    class Meta:
        model = TrailReview
        fields = ['review', 'star_rating']
        # hide the star_rating field
        widgets = {
            'star_rating': forms.HiddenInput()
        }
    
    
