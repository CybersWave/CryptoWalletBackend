from django.urls import path, re_path, include
from djoser import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)


from .views import (
    VerifyCodeView, 
    ResendCodeView, 
    PublicSetPasswordView,
    RecoveryRequestView,
    RecoverySetPasswordView,
    ResetPinRequestView,
    ResetPinVerifyView
)
djoser_urls = [
    path('users/', views.UserViewSet.as_view({'post': 'create'}), name='user-register'),

    path('users/me/', views.UserViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy',
    }), name='user-me'),

    path('users/set_password/', views.UserViewSet.as_view({'post': 'set_password'}), name='set-password'),
]



jwt_urls = [
    path('token/obtain/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]

custom_urls = [
    path('verify-code/', VerifyCodeView.as_view(), name='verify-code'),
    path('resend-code/', ResendCodeView.as_view(), name='resend-code'),
    path('public-set-password/', PublicSetPasswordView.as_view(), name='public-set-password'),

    path('recovery-request/', RecoveryRequestView.as_view(), name='recovery-request'),
    path('recovery-reset-password/', RecoverySetPasswordView.as_view(), name='recovery-reset-password'),

    path('reset-pin-request/', ResetPinRequestView.as_view(), name='reset-pin-request'),
    path('reset-pin-verify/', ResetPinVerifyView.as_view(), name='reset-pin-verify'),
]


urlpatterns = djoser_urls + jwt_urls + custom_urls
