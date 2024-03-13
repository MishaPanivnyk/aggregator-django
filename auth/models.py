from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    logo = models.ImageField(upload_to='logos/', null=True, blank=True)