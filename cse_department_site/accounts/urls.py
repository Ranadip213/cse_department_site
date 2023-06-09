from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register_page, name = 'register'),
 
    path('register/student/', views.student_form, name='register_student'),
    
    path('register/alumni/', views.alumni_form, name='register_alumni'),
    
    path('register/staff/', views.staff_form, name='register_staff'),
    path('login', views.login_page, name = 'login'),
    path('logout', views.logoutUser, name="logout"),
]