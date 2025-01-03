from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Result, Text
from django.contrib.auth.models import User
from .serializers import UserSerializer, TextSerializer, ResultSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.serializers import ModelSerializer

class UserList(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

class RandomTextView(generics.ListAPIView):
    queryset = Text.objects.order_by('?')[:1]
    serializer_class = TextSerializer
    permission_classes = [IsAuthenticated]

# Widok do zapisywania wyników
class ResultCreateView(generics.CreateAPIView):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer
    permission_classes = [IsAuthenticated]

# Widok do pobierania wyników użytkownika
class UserResultsView(generics.ListAPIView):
    serializer_class = ResultSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Result.objects.filter(user=user)

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