from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from .models import UserProfile
        
class SignupSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
        
class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id']
        
class UserProfileSerializer(ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'
        
    