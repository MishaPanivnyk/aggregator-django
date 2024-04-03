from rest_framework import serializers
from .models import University

class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = '__all__'

class TopUniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = '__all__'