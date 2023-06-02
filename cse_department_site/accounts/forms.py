from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import User, StudentProfile,StaffProfile,AlumniProfile

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields= ['username', 'email', 'password']