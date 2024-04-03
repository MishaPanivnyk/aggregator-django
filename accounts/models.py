# accounts/models.py

from django.contrib.auth.models import AbstractUser
from django.db import models
from cloudinary.models import CloudinaryField

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    imageUrl = CloudinaryField("image", blank=True)
    isCreator = models.BooleanField(default=False, blank=True)
    compareUniversities = models.JSONField(default=list, blank=True)
    def __str__(self):
        return self.username