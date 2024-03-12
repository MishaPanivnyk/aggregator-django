from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.CharField(max_length=255)
    imageUrl = models.ImageField(upload_to='images/', null=True, blank=True)
    category = models.CharField(max_length=255)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title