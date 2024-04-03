from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from .models import University, TopUniversity
from .serializers import UniversitySerializer, TopUniversitySerializer
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
    
@api_view(['GET'])
def university_search(request):
    if request.method == 'GET':
        query_params = request.query_params
        search_query = query_params.get('query', None)
        
        if search_query is not None:
            queryset = University.objects.filter(universityName__icontains=search_query)
            serializer = UniversitySerializer(queryset, many=True)
            return Response(serializer.data)
        else:
            return Response({"error": "Query parameter 'query' is required"}, status=status.HTTP_400_BAD_REQUEST)
      
@api_view(['GET'])
def university_detail(request, pk):
    university = get_object_or_404(University, pk=pk)
    serializer = UniversitySerializer(university)
    response = Response(serializer.data)
    return response


@api_view(['GET'])
def topUniversities(request):
    if request.method == 'GET':
        queryset = TopUniversity.objects.all()
        serializer = TopUniversitySerializer(queryset, many=True)
        return Response(serializer.data)

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def university_create(request):
    if request.method == 'POST':
        serializer = TopUniversitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 