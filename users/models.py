from django.db import models
from django.contrib.auth.models import AbstractUser

# About DATA
# Create your models here.

class User(AbstractUser):
    '''Custom User Model''' #'''
    
    avatar = models.ImageField(null = True)
    gender = models.CharField(max_length=10, null = True)
    bio = models.TextField(null = True)