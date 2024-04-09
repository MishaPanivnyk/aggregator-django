from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Review
from .serializers import ReviewSerializer
from universities.models import University
from rest_framework.views import APIView

def updateInfo(University, Rating):
    University.reviewCount += 1
    University.rating = (University.rating * (University.reviewCount - 1) + Rating ) / University.reviewCount
    University.save()


def minusReview(University, Rating):
    if University.reviewCount > 0:
        University.reviewCount -= 1
        if University.reviewCount == 0:
            University.rating = 0
        else:
            University.rating = (University.rating * (University.reviewCount + 1) - Rating) / University.reviewCount
        University.save()

class CreateReviewView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            university = serializer.validated_data['university']
            updateInfo(university, serializer.validated_data['rating'])
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GetAllReviewsView(APIView):
    def get(self, request):
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)


class GetUniversityReviewsView(APIView):
    def get(self, request, university_id):
        reviews = Review.objects.filter(university_id=university_id)
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)

class GetUserReviewsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, user_id):
        reviews = Review.objects.filter(user_id=user_id)
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)


class DeleteReviewView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, review_id):
        try:
            review = Review.objects.get(pk=review_id)
        except Review.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if review.user == request.user or request.user.isModerator:
            university = review.university
            rating = review.rating
            review.delete()
            minusReview(university, rating)
            return Response({"message": "Review was successfully deleted"}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "You don't have permission to delete this review."}, status=status.HTTP_403_FORBIDDEN)