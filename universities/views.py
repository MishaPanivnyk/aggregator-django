from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from .models import University, TopUniversity
from .serializers import UniversitySerializer, TopUniversitySerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from accounts.models import CustomUser
from accounts.serializers import UserSerializer

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

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_to_compare(request):
    if request.method == 'POST':
        user = request.user
        required_fields = {'university_id'}
        missing_fields = required_fields - set(request.data.keys())
        university_id = request.data['university_id']
        if len(user.compareUniversities) >= 3:
            return Response({'error': "Number of compared universities is out of range"}, status=status.HTTP_409_CONFLICT)
        if missing_fields:
            return Response({'error': f"Missing required fields: {', '.join(missing_fields)}"}, status=status.HTTP_400_BAD_REQUEST)
        if university_id in [uni['id'] for uni in user.compareUniversities]:
            return Response({'error': "University already in your comparison list"}, status=status.HTTP_409_CONFLICT)
        

        try:
            university = University.objects.get(pk=university_id)
        except University.DoesNotExist:
            return Response({'error': "University not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = UniversitySerializer(university)
        user = request.user
        user.compareUniversities.append(serializer.data)
        user.save()

            
        return Response(serializer.data)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def remove_from_compare(request):
    university_id = request.data['university_id']
    user = request.user

    for university in user.compareUniversities:
        if university['id'] == university_id:  # Access ID using dictionary key
            user.compareUniversities.remove(university)
            user.save()
            return Response({'success': "University removed from your comparison list"})

    return Response({'error': "University not found in your comparison list"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def all_compared_universities(request):
    user = request.user
    return Response(user.compareUniversities)