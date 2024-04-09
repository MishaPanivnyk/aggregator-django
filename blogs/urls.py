from django.urls import path
from .views import BlogDetailView, BlogDeleteView, BlogsView, BlogCreateView

urlpatterns = [
    path('blogs/', BlogsView.as_view(), name='register'),    
    path('blogs/create/', BlogCreateView.as_view(), name='blog-create'),
    path('blogs/<str:pk>/', BlogDetailView.as_view(), name='blog-detail'),
    path('blogs/<str:pk>/delete/', BlogDeleteView.as_view(), name='blog-delete'),
] 