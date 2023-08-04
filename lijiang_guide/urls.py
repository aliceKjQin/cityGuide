from django.urls import path

from . import views

app_name = 'lijiang_guide'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Hike page
    path('hike/', views.hike, name='hike'),
    # Cafe page
    path('cafe/', views.cafe, name='cafe'),
]