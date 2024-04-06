# accounts/serializers.py

import re
from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth.password_validation import validate_password

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'password', 'imageUrl', 'last_name', 'first_name', 'compareUniversities']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = CustomUser(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    
class PatchUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'password', 'imageUrl', 'last_name', 'first_name', 'isCreator']
        extra_kwargs = {
            'password': {'write_only': True},
            'username': {'required': False},
            'email': {'required': False},
            'last_name': {'required': False},
            'first_name': {'required': False},
            'isCreator': {'required': False},
        }

class PasswordResetSerializer(serializers.Serializer):
    new_password = serializers.CharField(max_length=25, write_only=True)

    def validate_new_password(self, value):
        if len(value) < 8:
            raise serializers.ValidationError("Password must be at least 8 characters long.")
        if not re.match(r'^[A-Za-z0-9!@#$%^&*()_+=-]+$', value):
            raise serializers.ValidationError("Password can only contain Latin letters, numbers, and some special characters.")
        validate_password(value)
        return value