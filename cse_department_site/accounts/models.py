from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User

class User(AbstractUser):
    is_student= models.BooleanField(default=False)
    is_staff= models.BooleanField(default=False)
    is_faculty= models.BooleanField(default=False)
    is_alumni= models.BooleanField(default=False)

class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name= models.CharField(max_length=100)
    id_number= models.CharField(max_length=12)
    Academic_year= models.CharField(max_length=50)
    phone_number=models.IntegerField((""))
    email=models.EmailField((""), max_length=254)

    # Add student-specific fields
    pass
class StaffProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name= models.CharField(max_length=100)
    phone_number= models.IntegerField((""))
    email=models.EmailField((""), max_length=254)
    subject= models.CharField((""), max_length=50)


    # Add staff-specific fields
    pass            

class AlumniProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name= models.CharField(max_length=100)
    phone_number=models.IntegerField((""))
    email=models.EmailField((""), max_length=254)
    academic_year= models.CharField(max_length=100)
    company= models.CharField(max_length=100)

    # Add alumni-specific fields
    pass