from django.urls import path
from .views import CreateReviewView, GetUniversityReviewsView, DeleteReviewView, GetAllReviewsView, GetUserReviewsView

urlpatterns = [
    path('create-review/', CreateReviewView.as_view(), name='create_review'),
    path('universities/<str:university_id>/reviews/', GetUniversityReviewsView.as_view(), name='university_reviews'),
    path('review/<int:review_id>/delete/', DeleteReviewView.as_view(), name='delete_review'),
    path('reviews/', GetAllReviewsView.as_view(), name='all_reviews'),
    path('api/profile/<int:user_id>/reviews/', GetUserReviewsView.as_view(), name='user_reviews'),
    
]