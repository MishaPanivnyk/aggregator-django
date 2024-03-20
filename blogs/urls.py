from django.urls import path
from .views import blog_detail, blog_delete, blogs, blog_create

urlpatterns = [
    path('blogs/', blogs, name='register'),    
    path('blogs/create/', blog_create, name='blog-create'),
    path('blogs/<str:pk>/', blog_detail, name='blog-detail'),
    path('blogs/<str:pk>/delete/', blog_delete, name='blog-delete'),

] 