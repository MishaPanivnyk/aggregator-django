from django.shortcuts import render
from rest_framework import generics
from django.shortcuts import render
from .models import Blog
from .serializers import BlogsSerializer

# Create your views here.

class BlogAPIView(generics.ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogsSerializer





