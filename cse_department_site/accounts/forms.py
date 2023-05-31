from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import User, StudentProfile,StaffProfile,AlumniProfile

class StudentProfileSignUpForm(UserCreationForm):
    name=forms.CharField(required=True)
    id_number=forms.CharField(required=True)
    id_number=forms.CharField(required=True)
    Academic_year=forms.CharField(required=True)
    phone_number=forms.CharField(required=True)
    email=forms.CharField(required=True)
  
    class Meta(UserCreationForm.Meta):
        model = User
 
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        
        user.is_student = True
        user.save()
        student = StudentProfile.objects.create(user=user)
        
        student.save()
 
        return student
    
    class StaffProfileSignUpForm(UserCreationForm):
      name=forms.CharField(required=True)
      phone_number=forms.IntegerField(required=True)
      email=forms.CharField(required=True)
      subject= forms.CharField(required=True)
  
    class Meta(UserCreationForm.Meta):
        model = User
 
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        
        user.is_staff = True
        user.save()
        staff = StaffProfile.objects.create(user=user)
        
        staff.save()
 
        return staff
    
    class AlumniProfileSignUpForm(UserCreationForm):
      name=forms.CharField(required=True)
      phone_number=forms.IntegerField(required=True)
      email=forms.EmailField( required=False)
      academic_year= forms.CharField(required=True)
      company= forms.CharField(max_length=100)
    
      class Meta(UserCreationForm.Meta):
          model = User
  
      @transaction.atomic
      def save(self):
          user = super().save(commit=False)
          
          user.is_alumni = True
          user.save()
          alumni = AlumniProfile.objects.create(user=user)
          
          alumni.save()
  
          return alumni