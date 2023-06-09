from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User


class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('student', 'Student'),
        ('staff', 'Staff Member'),
        ('alumni', 'Alumni'),
    )

    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)