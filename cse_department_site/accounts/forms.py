from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import CustomUser, Student, Alumni, Staff

class CreateUserForm(UserCreationForm):
	class Meta:
		model = CustomUser
		fields = ['username', 'email', 'password1', 'password2', 'user_type']
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['student_field']

class AlumniForm(forms.ModelForm):
    class Meta:
        model = Alumni
        fields = ['alumni_field']

class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ['staff_field']		