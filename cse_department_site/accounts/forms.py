from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Users, Student, Alumni, Staff


class CreateUserForm(UserCreationForm):
    """
    Form for user registration.
    Inherits from UserCreationForm provided by Django.
    """
    class Meta:
        model = Users
        fields = ['username', 'email', 'password1', 'password2', 'user_type']


class StudentForm(forms.ModelForm):
    """
    Form for student registration.
    Inherits from ModelForm provided by Django.
    """
    class Meta:
        model = Student
        fields = '__all__'


class AlumniForm(forms.ModelForm):
    """
    Form for alumni registration.
    Inherits from ModelForm provided by Django.
    """
    class Meta:
        model = Alumni
        fields = '__all__'


class StaffForm(forms.ModelForm):
    """
    Form for staff registration.
    Inherits from ModelForm provided by Django.
    """
    class Meta:
        model = Staff
        fields = '__all__'
