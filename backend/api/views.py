from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User, Result, Text
from .serializers import UserSerializer, TextSerializer, ResultSerializer
from rest_framework import generics

class UserList(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

class RandomTextView(generics.ListAPIView):
    queryset = Text.objects.order_by('?')[:1]
    serializer_class = TextSerializer

# Widok do zapisywania wyników
class ResultCreateView(generics.CreateAPIView):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer

# Widok do pobierania wyników użytkownika
class UserResultsView(generics.ListAPIView):
    serializer_class = ResultSerializer

    def get_queryset(self):
        user = self.request.user
        return Result.objects.filter(user=user)