# accounts/models.py

from django.contrib.auth.models import AbstractUser
from django.db import models
from cloudinary.models import CloudinaryField

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    imageUrl = CloudinaryField("image")
    def __str__(self):
        return self.username