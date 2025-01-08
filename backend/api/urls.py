from django.urls import path
from .views import UserList, RandomTextView, ResultCreateView, UserResultsView, RegisterView, AddTextView, TextListView, EditTextView, DeleteTextView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('users/', UserList.as_view(), name='user-list'),
    path('text/', RandomTextView.as_view(), name='random_text'),
    path('results/', ResultCreateView.as_view(), name='create_result'),
    path('user/results/', UserResultsView.as_view(), name='user_results'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('register/', RegisterView.as_view(), name='register'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('texts/', AddTextView.as_view(), name='add-text'),
    path('textlist/', TextListView.as_view(), name='text_list'),
    path('texts/<int:pk>/', EditTextView.as_view(), name='edit_text'),
    path('texts/<int:pk>/', DeleteTextView.as_view(), name='delete_text'),  
]