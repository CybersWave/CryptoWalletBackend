from random import randint
from django.contrib.auth import get_user_model
from django.apps import apps



def generate_unique_userid():
    if not apps.ready or not apps.is_installed('account'):
        return str(randint(10**15, (10**16)-1))

    from django.contrib.auth import get_user_model
    User = get_user_model()

    while True:
        userid = str(randint(10**15, (10**16)-1))
        try:
            if not User.objects.filter(userID=userid).exists():
                return userid
        except Exception:
            return userid

def generate_verification_code(self):
    self.verification_code = str(randint(100000, 999999))
    self.verification_expiry = timezone.now() + timedelta(minutes=30)
    self.is_active = False
    self.save()
