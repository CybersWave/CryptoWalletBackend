from django.urls import path
from account.views import UserProfileView

urlpatterns = [
    path('', UserProfileView.as_view(), name="user profile")
]
