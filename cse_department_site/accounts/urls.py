from django.urls import path
from . import views

urlpatterns = [
     path('register', views.register_page, name = 'register'),
     path('logout', views.logoutUser, name="logout"),
]