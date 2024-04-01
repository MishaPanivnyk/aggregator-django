# accounts/serializers.py

from rest_framework import serializers
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'password', 'imageUrl', 'last_name', 'first_name']
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
        fields = ['id', 'username', 'email', 'password', 'imageUrl', 'last_name', 'first_name']
        extra_kwargs = {
            'password': {'write_only': True},
            'username': {'required': False},
            'email': {'required': False},
            'last_name': {'required': False},
            'first_name': {'required': False},
        }