from django.urls import path
from .views import UserList, RandomTextView, UserResultsView, RegisterView, AddTextView, TextListView, EditTextView, DeleteTextView, ResultView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('users/', UserList.as_view(), name='user-list'),
    path('text/', RandomTextView.as_view(), name='random_text'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('register/', RegisterView.as_view(), name='register'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('add-text/', AddTextView.as_view(), name='add-text'),
    path('textlist/', TextListView.as_view(), name='text_list'),
    path('texts/<int:pk>/', EditTextView.as_view(), name='edit_text'),
    path('texts/<int:pk>/delete/', DeleteTextView.as_view(), name='delete_text'),
    path('result/', ResultView.as_view(), name='result'),
    path('results/', UserResultsView.as_view(), name='user_results'),
]