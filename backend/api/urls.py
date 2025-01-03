from django.urls import path
from .views import UserList, RandomTextView, ResultCreateView, UserResultsView

urlpatterns = [
    path('users/', UserList.as_view(), name='user-list'),
    path('text/', RandomTextView.as_view(), name='random_text'),
    path('results/', ResultCreateView.as_view(), name='create_result'),
    path('user/results/', UserResultsView.as_view(), name='user_results')
]