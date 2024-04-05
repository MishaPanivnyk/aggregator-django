from django.db import models
from accounts.models import CustomUser
from universities.models import University

class Review(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True)
    university = models.ForeignKey(University, on_delete=models.CASCADE, related_name='reviews_stored')
    rating = models.PositiveSmallIntegerField(default=0, blank=True)
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"({self.created_at}) {self.user.username}: ({self.rating}) {self.comment} ({self.university.universityName})"
