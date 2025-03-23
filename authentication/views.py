from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.utils import timezone

from datetime import timedelta

from account.serializers import PublicSetPasswordSerializer, RecoveryRequestSerializer, RecoverySetPasswordSerializer

from .models import User, VerificationCode
from .utils import generate_verification_code


User = get_user_model()


class RecoveryRequestView(APIView):
    def post(self, request):
        serializer = RecoveryRequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"detail": "Recovery code sent to email."})
        return Response(serializer.errors, status=400)


class RecoverySetPasswordView(APIView):
    def post(self, request):
        email = request.data.get('email')
        code = request.data.get('code')

        if not email or not code:
            return Response({"error": "Email and verification code are required."}, status=400)

        try:
            user = User.objects.get(email=email)

            verification = VerificationCode.objects.filter(
                user=user,
                code=code,
                purpose='password_recovery'
            ).order_by('-created_at').first()

            if not verification:
                return Response({"error": "Invalid verification code."}, status=400)

            if verification.is_expired():
                verification.delete()
                return Response({"error": "Verification code has expired."}, status=400)

            serializer = RecoverySetPasswordSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(email=email)
                verification.delete()
                return Response({"detail": "Password reset successful."})
            return Response(serializer.errors, status=400)

        except User.DoesNotExist:
            return Response({"error": "User not found."}, status=404)

class PublicSetPasswordView(APIView):
    def post(self, request):
        serializer = PublicSetPasswordSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"detail": "Password set successfully."})
        return Response(serializer.errors, status=400)


class VerifyCodeView(APIView):
    def post(self, request):
        email = request.data.get('email')
        code = request.data.get('code')
        purpose = request.data.get('purpose')

        if not email or not code or not purpose:
            return Response({"error": "Email, code, and purpose are required."}, status=400)

        try:
            user = User.objects.get(email=email)

            verification = VerificationCode.objects.filter(
                user=user,
                code=code,
                purpose=purpose
            ).order_by('-created_at').first()

            if not verification:
                return Response({"error": "No valid verification code found for this purpose."}, status=400)

            if verification.is_expired():
                verification.delete()
                return Response({"error": "Verification code has expired."}, status=400)

            if purpose == 'email_verification':
                user.is_active = True
                user.save()
            elif purpose == 'password_recovery':
                return Response({"detail": f"{purpose.replace('_', ' ').capitalize()} successful."}, status=200)
            else:
                return Response({"error": "Unsupported verification purpose."}, status=400)

            verification.delete()

            return Response({"detail": f"{purpose.replace('_', ' ').capitalize()} successful."}, status=200)

        except User.DoesNotExist:
            return Response({"error": "User not found."}, status=404)


class ResetPinRequestView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        generate_verification_code(user, purpose='reset_pin')

        return Response({"detail": "Verification code sent to your email."})


class ResetPinVerifyView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        code = request.data.get('code')
        user = request.user

        if not code:
            return Response({"error": "Code is required."}, status=400)

        verification = VerificationCode.objects.filter(
            user=user,
            code=code,
            purpose='reset_pin'
        ).order_by('-created_at').first()

        if not verification:
            return Response({"error": "Invalid verification code."}, status=400)

        if verification.is_expired():
            verification.delete()
            return Response({"error": "Verification code has expired."}, status=400)

        verification.delete()

        return Response({"detail": "PIN reset verification successful."})



class ResendCodeView(APIView):
    def post(self, request):
        email = request.data.get('email')

        try:
            user = User.objects.get(email=email)
            generate_verification_code(user)
            return Response({"detail": "New code sent to email."})
        except User.DoesNotExist:
            return Response({"error": "User not found."}, status=404)


# NOTE: Cront Tab
'''
if timezone.now() - user.code_created_at > timedelta(minutes=5):
    user.verification_code = None
    user.code_created_at = None
    user.save()
    return Response({"error": "Code has expired."}, status=400)
'''