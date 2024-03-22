from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from .models import Blog
from .serializers import BlogsSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

# Create your views here.

@api_view(['GET'])
def blogs(request):
    if request.method == 'GET':
        queryset = Blog.objects.all()
        serializer = BlogsSerializer(queryset, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def blog_detail(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    serializer = BlogsSerializer(blog)
    return Response(serializer.data)


@api_view(['DELETE'])
def blog_delete(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    if request.method == 'DELETE':
        blog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


import cloudinary.uploader  # Import the cloudinary module

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def blog_create(request):
    if request.method == 'POST':
        serializer = BlogsSerializer(data=request.data)
        if serializer.is_valid():
            image = request.FILES.get('imageUrl')  # Access the uploaded image
            if image:
                uploaded_image = cloudinary.uploader.upload(image)  # Upload to Cloudinary
                print(uploaded_image['url'])
                serializer.validated_data['imageUrl'] = uploaded_image['secure_url'][50:]  # Update URL
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)