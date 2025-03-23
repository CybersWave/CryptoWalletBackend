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

