from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Result, Text
from django.contrib.auth.models import User
from .serializers import UserSerializer, TextSerializer, ResultSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
import random
from django.db.models import Avg

class UserList(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

class RandomTextView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        texts = Text.objects.all()
        if not texts.exists():
            return Response({"detail": "No texts available"}, status=status.HTTP_404_NOT_FOUND)
        random_text = random.choice(texts)
        serializer = TextSerializer(random_text)
        return Response(serializer.data)

class RegisterSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer

class AddTextView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = TextSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class TextListView(generics.ListAPIView):
    queryset = Text.objects.all()
    serializer_class = TextSerializer
    permission_classes = [IsAuthenticated]

class EditTextView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Text.objects.all()
    serializer_class = TextSerializer
    permission_classes = [IsAuthenticated]

class DeleteTextView(generics.DestroyAPIView):
    queryset = Text.objects.all()
    serializer_class = TextSerializer
    permission_classes = [IsAuthenticated]

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Result
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

class ResultView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data

        wpm = data.get('wpm')
        accuracy = data.get('accuracy')

        if wpm is None or accuracy is None:
            return Response({"error": "WPM and accuracy are required"}, status=status.HTTP_400_BAD_REQUEST)

        result = Result.objects.create(user=request.user, wpm=wpm, accuracy=accuracy)
        result.save()

        return Response({"message": "Result saved successfully"}, status=status.HTTP_201_CREATED)    
    
class UserResultsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        results = Result.objects.filter(user=request.user)
        data = [
            {
                'wpm': result.wpm,
                'accuracy': result.accuracy,
                'created_at': result.created_at,
            }
            for result in results
        ]
        return Response(data)