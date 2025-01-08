from rest_framework import serializers
from .models import User, Text, Result

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        
class TextSerializer(serializers.ModelSerializer):
    class Meta:
        model = Text
        fields = ['id', 'content']

class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = ['id', 'user', 'text', 'wpm', 'accuracy', 'created_at']