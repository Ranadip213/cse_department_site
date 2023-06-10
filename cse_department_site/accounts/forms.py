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
        fields = '__all__'

class AlumniForm(forms.ModelForm):
    class Meta:
        model = Alumni
        fields = '__all__'

class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = '__all__'