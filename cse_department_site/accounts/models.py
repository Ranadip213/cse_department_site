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

class Alumni(models.Model):
    user = models.OneToOneField(Users, on_delete=models.CASCADE, related_name='alumni')
    alumni_field = models.CharField(max_length=100)

class Staff(models.Model):
    user = models.OneToOneField(Users, on_delete=models.CASCADE, related_name='staff')
    staff_field = models.CharField(max_length=100)