from django.urls import path
from .views import blog_detail, blogs

urlpatterns = [
    path('blogs/', blogs, name='register'),
    path('blogs/<pk>/', blog_detail, name='blog-detail'),
]