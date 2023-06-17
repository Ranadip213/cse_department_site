from django.urls import path
from . import views

urlpatterns = [
    path('clubs', views.clubes_page, name = 'clubs'),
    path('gallery', views.gallery_images, name = 'gallery'),
]