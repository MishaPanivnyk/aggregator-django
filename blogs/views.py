from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from .models import Blog
from .serializers import BlogsSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
import cloudinary.uploader
# Create your views here.

class BlogsView(APIView):
    def get(self, request):
        queryset = Blog.objects.all()
        serializer = BlogsSerializer(queryset, many=True)
        return Response(serializer.data)

class BlogDetailView(APIView):
    def get(self, request, pk):
        blog = get_object_or_404(Blog, pk=pk)
        serializer = BlogsSerializer(blog)
        response = Response(serializer.data)
        return response

class BlogDeleteView(APIView):
    def delete(self, request, pk):
        blog = get_object_or_404(Blog, pk=pk)
        blog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class BlogCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = BlogsSerializer(data=request.data)
        if serializer.is_valid():
            image = request.FILES.get('imageUrl')
            if image:
                uploaded_image = cloudinary.uploader.upload(image)
                serializer.validated_data['imageUrl'] = uploaded_image['secure_url'][50:]
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)