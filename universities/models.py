import os
from django.db import models

# Create your models here.
def generate_uuid():
    return ''.join([format(byte, '02x') for byte in os.urandom(8)])

class University(models.Model):
    id = models.CharField(primary_key=True, default=generate_uuid, editable=False)
    universityName = models.CharField(max_length=200)
    img = models.URLField()
    location = models.CharField(max_length=200)
    desc = models.TextField()
    accreditationLevel = models.CharField(max_length=50)
    rating = models.FloatField()
    reviews = models.JSONField()
    type = models.CharField(max_length=100)
    features = models.TextField()
    remoteEducation = models.CharField()
    price = models.CharField(max_length=100)
    specialties = models.JSONField()
    contactInfo = models.JSONField()
    website = models.URLField()
