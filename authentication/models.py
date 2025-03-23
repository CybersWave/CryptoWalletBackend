from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from datetime import timedelta

User = get_user_model()


class VerificationCode(models.Model):
    PURPOSE_CHOICES = [
        ('email_verification', 'Email Verification'),
        ('password_recovery', 'Password Recovery'),
        ('reset_pin', 'Reset Pin Code'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='verification_codes')
    code = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    purpose = models.CharField(max_length=32, choices=PURPOSE_CHOICES, null=True)


    def is_expired(self):
        return timezone.now() > self.created_at + timedelta(minutes=15)

    def __str__(self):
        return f"{self.user.email} - {self.code}"