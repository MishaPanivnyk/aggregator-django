from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from .models import University
from .serializers import UniversitySerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

# Create your views here.

@api_view(['GET'])
def universities(request):
    if request.method == 'GET':
        queryset = University.objects.all()
        serializer = UniversitySerializer(queryset, many=True)
        return Response(serializer.data)
    
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def university_create(request):
    if request.method == 'POST':
        serializer = UniversitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 