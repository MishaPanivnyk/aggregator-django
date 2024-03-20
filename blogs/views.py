from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from .models import Blog
from .serializers import BlogsSerializer
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['GET'])
def blogs(request):
    queryset = Blog.objects.all()
    serializer = BlogsSerializer(queryset, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def blog_detail(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    serializer = BlogsSerializer(blog)
    return Response(serializer.data)
