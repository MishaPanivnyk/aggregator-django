from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from .models import University, TopUniversity
from .serializers import UniversitySerializer, TopUniversitySerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

# Create your views here.

class UniversityList(APIView):
    def get(self, request):
        queryset = University.objects.all()
        serializer = UniversitySerializer(queryset, many=True)
        return Response(serializer.data)
    
class UniversityCreate(APIView):
    permission_classes = [IsAuthenticated]  # Require authentication for this view

    def post(self, request):
        serializer = UniversitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UniversitySearch(APIView):
    def get(self, request):
        query_params = request.query_params
        search_query = query_params.get('query', None)

        if search_query is not None:
            queryset = University.objects.filter(universityName__icontains=search_query)
            serializer = UniversitySerializer(queryset, many=True)
            return Response(serializer.data)
        else:
            return Response({"error": "Query parameter 'query' is required"}, status=status.HTTP_400_BAD_REQUEST)
      
class UniversityDetail(APIView):
    def get(self, request, pk):
        try:
            university = University.objects.get(pk=pk)
        except University.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = UniversitySerializer(university)
        return Response(serializer.data)

class TopUniversityList(APIView):
    def get(self, request):
        queryset = TopUniversity.objects.all()
        serializer = TopUniversitySerializer(queryset, many=True)
        return Response(serializer.data)

class AddToCompareView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        required_fields = {'university_id'}
        missing_fields = required_fields - set(request.data.keys())
        if missing_fields:
            return Response({'error': f"Missing required fields: {', '.join(missing_fields)}"}, status=status.HTTP_400_BAD_REQUEST)

        university_id = request.data['university_id']
        user = request.user

        if len(user.compareUniversities) >= 3:
            return Response({'error': 'Number of compared universities is out of range'}, status=status.HTTP_409_CONFLICT)

        if university_id in [uni['id'] for uni in user.compareUniversities]:
            return Response({'error': 'University already in your comparison list'}, status=status.HTTP_409_CONFLICT)

        try:
            university = University.objects.get(pk=university_id)
        except University.DoesNotExist:
            return Response({'error': 'University not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = UniversitySerializer(university)
        user.compareUniversities.append(serializer.data)
        user.save()
        return Response(serializer.data)

class RemoveFromCompareView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request):
        try:
            university_id = request.data['university_id']
        except KeyError:
            return Response({'error': 'University ID is required'}, status=status.HTTP_400_BAD_REQUEST)

        user = request.user
        found = False
        for university in user.compareUniversities:
            if university['id'] == university_id:
                user.compareUniversities.remove(university)
                user.save()
                found = True
                return Response({'success': 'University removed from your comparison list'}, status=status.HTTP_200_OK)
        if not found:
            return Response({'error': 'University not found in your comparison list'}, status=status.HTTP_404_NOT_FOUND)

class AllComparedUniversitiesView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        user = request.user
        return Response(user.compareUniversities)
