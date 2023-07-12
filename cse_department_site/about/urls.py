from django.urls import path
from . import views

urlpatterns = [
    path('gallery', views.gallery_images, name='gallery'),
    path('student', views.student, name='student'),
    path('facalty', views.facalty, name='facalty'),
    path('alumai', views.alumai, name='alumai'),
]
