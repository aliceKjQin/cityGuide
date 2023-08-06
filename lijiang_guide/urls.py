from django.urls import path

from . import views

app_name = 'lijiang_guide'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Hiking page
    path('hiking/', views.hiking, name='hiking'),
    # Particular trail page
    path('hiking/<int:trail_id>', views.trail, name='trail'),
    # Particular trail review page
    path('trail_reviews/<int:trail_id>', views.trail_reviews, name='trail_reviews'),
    # Cafe page
    path('cafe/', views.cafe, name='cafe'),
]