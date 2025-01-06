from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Result, Text
from django.contrib.auth.models import User
from .serializers import UserSerializer, TextSerializer, ResultSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status
from rest_framework.serializers import ModelSerializer
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

class ResultCreateView(generics.CreateAPIView):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        text_id = self.request.data.get('text')
        try:
            text = Text.objects.get(id=text_id)
        except Text.DoesNotExist:
            raise serializers.ValidationError("Text with this ID does not exist.")
        serializer.save(user=user, text=text)

class UserResultsView(generics.ListAPIView):
    serializer_class = ResultSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return Result.objects.filter(user_id=user_id)

class UserStatisticsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, user_id):
        results = Result.objects.filter(user_id=user_id)
        avg_wpm = results.aggregate(Avg('wpm'))['wpm__avg']
        avg_accuracy = results.aggregate(Avg('accuracy'))['accuracy__avg']
        return Response({
            'average_wpm': avg_wpm,
            'average_accuracy': avg_accuracy,
            'total_results': results.count()
        })

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