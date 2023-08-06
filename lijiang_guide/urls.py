from django.urls import path

from . import views

app_name = 'lijiang_guide'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Hiking page
    path('hiking/', views.hiking, name='hiking'),
    # Individual hiking spot page
    path('hiking/<int:trail_id>', views.Trail, name='trail'),
    # Cafe page
    path('cafe/', views.cafe, name='cafe'),
]