from django.contrib.auth.models import AbstractUser
from django.db import models


class Users(AbstractUser):
    USER_TYPE_CHOICES = (
        ('student', 'Student'),
        ('staff', 'Staff Member'),
        ('alumni', 'Alumni'),
    )

    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)

    class Meta:
        verbose_name = 'Custom User'
        verbose_name_plural = 'Custom Users'

class Student(models.Model):
    user = models.OneToOneField(Users, on_delete=models.CASCADE, related_name='student')
    student_field = models.CharField(max_length=100)
    full_name= models.CharField(max_length=100)
    contact_number= models.IntegerField(max_length=10)
    year=models.IntegerField()
    email=models.EmailField(max_length=254)
    

class Alumni(models.Model):
    user = models.OneToOneField(Users, on_delete=models.CASCADE, related_name='alumni')
    alumni_field = models.CharField(max_length=100)
    full_name= models.CharField(max_length=100)
    contact_number= models.IntegerField(max_length=10)
    email=models.EmailField(max_length=254)
    specialization=models.CharField(max_length=100)

class Staff(models.Model):
    user = models.OneToOneField(Users, on_delete=models.CASCADE, related_name='staff')
    staff_field = models.CharField(max_length=100)
    full_name= models.CharField(max_length=100)
    contact_number= models.IntegerField(max_length=10)
    email=models.EmailField(max_length=254)
    current_company= models.CharField(max_length=100)
    graduation_year= models.IntegerField(max_length=100)
