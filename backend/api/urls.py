from django.urls import path
from .views import UserList, RandomTextView, ResultCreateView, UserResultsView, RegisterView, AddTextView

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
    path('texts/', AddTextView.as_view(), name='add-text')
]