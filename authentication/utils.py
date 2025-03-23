import random
from django.core.mail import send_mail
from .models import VerificationCode

def generate_verification_code(user, purpose):
    code = str(random.randint(100000, 999999))
    VerificationCode.objects.create(user=user, code=code, purpose=purpose)

    send_mail(
        subject="Your CryptoWallet Verification Code",
        message=f"Your verification code for {purpose.replace('_', ' ')} is: {code}",
        from_email="noreply@cryptowallet.com",
        recipient_list=[user.email],
    )