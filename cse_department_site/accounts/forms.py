from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import User,CustomUser

class CreateUserForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields= ['username', 'email', 'password', 'student_field', 'staff_field', 'alumni_field']


        def clean(self):
            cleaned_data= super().clean()
            user_type= cleaned_data.get('user_type')

            if user_type == 'student':
                if not cleaned_data.get('student_field'):
                    self.add_error('student_field', 'this field is requird for students')
            elif user_type == 'staff':
                if not cleaned_data.get('staff_field'):
                    self.add_error('staff_field', 'this field is required for staff members')
                elif user_type == 'alumni':
                    if not cleaned_data.get('alumni_field'):
                        self.add_error('alumni_field', 'this field is required for alumni')