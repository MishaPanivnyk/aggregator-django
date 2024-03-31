from django.urls import path
from .views import create_review, university_reviews, delete_review, all_reviews

urlpatterns = [
    path('create-review/', create_review, name='create_review'),
    path('universities/<str:university_id>/reviews/', university_reviews, name='university_reviews'),
    path('review/<int:review_id>/delete/', delete_review, name='delete_review'),
    path('reviews/', all_reviews, name='all_reviews')
]