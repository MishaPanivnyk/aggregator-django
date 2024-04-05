from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Review
from .serializers import ReviewSerializer
from universities.models import University

def updateInfo(University, Rating):
    University.reviewCount += 1
    University.rating = (University.rating * (University.reviewCount - 1) + Rating ) / University.reviewCount
    University.save()


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_review(request):
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        University = serializer.validated_data['university']
        updateInfo(University, serializer.validated_data['rating'])
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def all_reviews(request):
    reviews = Review.objects.all()
    serializer = ReviewSerializer(reviews, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def university_reviews(request, university_id):
    reviews = Review.objects.filter(university_id=university_id)
    serializer = ReviewSerializer(reviews, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_reviews(request, user_id):
    reviews = Review.objects.filter(user_id=user_id)
    serializer = ReviewSerializer(reviews, many=True)
    return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_review(request, review_id):
    try:
        review = Review.objects.get(pk=review_id)
    except Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if review.user != request.user:
        return Response({"error": "You don't have permission to delete this review."}, status=status.HTTP_403_FORBIDDEN)

    review.delete()
    University.reviewCount -= 1
    return Response(status=status.HTTP_204_NO_CONTENT)