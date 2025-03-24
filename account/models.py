from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.db.models.signals import post_save
from django.dispatch import receiver
import uuid

from .utils import generate_unique_userid


class CustomUserManager(BaseUserManager):
    def _create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    userID = models.CharField(max_length=16, unique=True, default=generate_unique_userid, editable=False)

    username = None
    email = models.EmailField(unique=True)
    img = models.ImageField(upload_to="images/avatars/", blank=True)
    phone_number = PhoneNumberField(blank=True)
    dob = models.DateField(blank=True, null=True)
    country = models.CharField(max_length=100, blank=True)
    email_verified = models.BooleanField(default=False, null=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']


class CryptoCurrency(models.Model):
    name = models.CharField(max_length=50)
    icon = models.ImageField(upload_to='images/cryptoIcons/')


class VirtualCurrency(models.Model):
    name = models.CharField(max_length=50)
    icon = models.ImageField(upload_to='images/virtualIcons/')


class CryptoWallet(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='crypto_wallet')


class VirtualWallet(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='virtual_wallet')


class CryptoWalletItem(models.Model):
    wallet = models.ForeignKey(CryptoWallet, on_delete=models.CASCADE, related_name="items")
    currency = models.ForeignKey(CryptoCurrency, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=20, decimal_places=8, default=0.0)

    class Meta:
        unique_together = ('wallet', 'currency')


class VirtualWalletItem(models.Model):
    wallet = models.ForeignKey(VirtualWallet, on_delete=models.CASCADE, related_name="items")
    currency = models.ForeignKey(VirtualCurrency, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=20, decimal_places=8, default=0.0)

    class Meta:
        unique_together = ('wallet', 'currency')








































# from django.contrib.auth.models import AbstractUser
# from django.db import models
# from phonenumber_field.modelfields import PhoneNumberField
# import uuid


# from .utils import generate_unique_userid

# class CustomUserManager(BaseUserManager):
#     def _create_user(self, email, password=None, **extra_fields):
#         if not email:
#             raise ValueError('The given email must be set')
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_user(self, email, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', False)
#         extra_fields.setdefault('is_superuser', False)
#         return self._create_user(email, password, **extra_fields)

#     def create_superuser(self, email, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)

#         if extra_fields.get('is_staff') is not True:
#             raise ValueError('Superuser must have is_staff=True.')
#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError('Superuser must have is_superuser=True.')

#         return self._create_user(email, password, **extra_fields)



# class CustomUser(AbstractUser):
#     userID =  models.CharField(max_length=16, unique=True, default=generate_unique_userid, editable=False)

#     username = None
#     email = models.EmailField(unique=True)
#     img = models.ImageField(upload_to="images/avatars/", blank=True)
#     phone_number = PhoneNumberField(blank=True)
#     dob = models.DateField(blank=True)
#     country = models.CharField(max_length=100)

#     objects = CustomUserManager()
    
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['first_name', 'last_name'] 




# class CryptoCurrency(models.Model):
#     icon = models.FileField(upload_to='images/cryptoIcons/')
#     address = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
#     amount = models.DecimalField(max_digits=5, decimal_places=7, default=0.0)


# class VirtualCurrency(models.Model):
#     icon = models.FileField(upload_to='images/cryptoIcons/')
#     address = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
#     amount = models.DecimalField(max_digits=5, decimal_places=7, default=0.0)



# class VirtualWallet(models.Model):
#     user = models.ForeignKey("CustomUser", on_delete=models.CASCADE)
#     address = models.ManyToManyField("VirtualCurrency", default=VirtualCurrency.objects.all())



# class CryptoWallet(models.Model):
#     user = models.ForeignKey("CustomUser", on_delete=models.CASCADE)
#     address = models.ManyToManyField("CryptoCurrency", default=CryptoCurrency.objects.all())

