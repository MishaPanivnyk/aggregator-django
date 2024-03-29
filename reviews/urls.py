from django.urls import path
from . import views

urlpatterns = [
    path('create-review/', views.create_review, name='create_review'),
    path('universities/<str:university_id>/reviews/', views.university_reviews, name='university_reviews'),
    path('review/<int:review_id>/delete/', views.delete_review, name='delete_review'),
]