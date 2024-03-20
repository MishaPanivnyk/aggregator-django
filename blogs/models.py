import os
from django.db import models
from tinymce.models import HTMLField
import uuid
from cloudinary.models import CloudinaryField
# Create your models here.

def generate_uuid():
    return ''.join([format(byte, '02x') for byte in os.urandom(8)])

class Blog(models.Model):
    id = models.CharField(primary_key=True, default=generate_uuid, editable=False)
    title = models.CharField(max_length=255)
    content = HTMLField()
    author = models.CharField(max_length=255)
    imageUrl = CloudinaryField('image')
    category = models.CharField(max_length=255)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title