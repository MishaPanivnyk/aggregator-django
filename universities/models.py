import os
from django.db import models

# Create your models here.
def generate_uuid():
    return ''.join([format(byte, '02x') for byte in os.urandom(8)])

class University(models.Model):
    id = models.CharField(primary_key=True, default=generate_uuid, editable=False)
    universityName = models.CharField(blank=True)
    img = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=200, blank=True)
    desc = models.TextField(blank=True)
    accreditationLevel = models.CharField(max_length=50, blank=True)
    reviewCount = models.IntegerField(blank=True, default=0)
    rating = models.FloatField(blank=True)
    type = models.CharField(max_length=100, blank=True)
    features = models.TextField(blank=True)
    remoteEducation = models.CharField(blank=True)
    price = models.CharField(max_length=100, blank=True)
    specialties = models.JSONField(blank=True)
    contactInfo = models.JSONField(blank=True)
    website = models.CharField(blank=True)

    def __str__(self):
        return self.universityName