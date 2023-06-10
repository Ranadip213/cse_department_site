from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Users, Student, Alumni, Staff

class CreateUserForm(UserCreationForm):
	class Meta:
		model = Users
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