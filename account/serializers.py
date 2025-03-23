from rest_framework import serializers
from djoser.serializers import UserCreateSerializer, SetPasswordSerializer
from djoser.serializers import SetPasswordSerializer

from django.core.mail import send_mail
from django.utils import timezone
from django.contrib.auth import get_user_model

from authentication.utils import generate_verification_code
from random import randint


from .models import (
    CryptoCurrency,
    VirtualCurrency,
    CryptoWallet,
    VirtualWallet,
    CryptoWalletItem,
    VirtualWalletItem
)

User = get_user_model()


class CryptoCurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = CryptoCurrency
        fields = ['id', 'name', 'icon']



class VirtualCurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = VirtualCurrency
        fields = ['id', 'name', 'icon']



class CryptoWalletItemSerializer(serializers.ModelSerializer):
    currency = CryptoCurrencySerializer()

    class Meta:
        model = CryptoWalletItem
        fields = ['currency', 'amount']



class VirtualWalletItemSerializer(serializers.ModelSerializer):
    currency = VirtualCurrencySerializer()

    class Meta:
        model = VirtualWalletItem
        fields = ['currency', 'amount']


class CryptoWalletSerializer(serializers.ModelSerializer):
    items = CryptoWalletItemSerializer(many=True, read_only=True)

    class Meta:
        model = CryptoWallet
        fields = ['items']


class VirtualWalletSerializer(serializers.ModelSerializer):
    items = VirtualWalletItemSerializer(many=True, read_only=True)

    class Meta:
        model = VirtualWallet
        fields = ['items']


class UserProfileSerializer(serializers.ModelSerializer):
    crypto_wallet = CryptoWalletSerializer(read_only=True)
    virtual_wallet = VirtualWalletSerializer(read_only=True)

    class Meta:
        model = User
        fields = [
            'userID', 'email', 'first_name', 'last_name', 'img',
            'phone_number', 'dob', 'country',
            'crypto_wallet', 'virtual_wallet'
        ]


class CustomUserCreateSerializer(UserCreateSerializer):
    email = serializers.EmailField()
    terms_accepted = serializers.BooleanField(write_only=True)

    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('email', 'terms_accepted')

    def validate(self, attrs):
        if not attrs.get('terms_accepted'):
            raise serializers.ValidationError("You must accept terms and conditions.")
        return attrs

    def create(self, validated_data):
        email = validated_data['email']

        user, created = User.objects.get_or_create(email=email)
        generate_verification_code(user)


        user.is_active = False
        user.save()

        return user

class PublicSetPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    repeat_password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        if attrs['password'] != attrs['repeat_password']:
            raise serializers.ValidationError("Passwords do not match.")
        return attrs

    def save(self):
        email = self.validated_data['email']
        password = self.validated_data['password']

        try:
            user = User.objects.get(email=email)
            if not user.is_active:
                raise serializers.ValidationError("Email not verified.")
            user.set_password(password)
            user.is_active = True
            user.save()
        except User.DoesNotExist:
            raise serializers.ValidationError("User not found.")




class CustomSetPasswordSerializer(SetPasswordSerializer):
    def validate(self, attrs):
        user = self.context['request'].user
        if not user.is_active:
            raise serializers.ValidationError("Please verify your email first.")
        return super().validate(attrs)



class RecoveryRequestSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate_email(self, value):
        if not User.objects.filter(email=value).exists():
            raise serializers.ValidationError("User with this email does not exist.")
        return value

    def save(self):
        user = User.objects.get(email=self.validated_data['email'])
        code = str(randint(100000, 999999))

        generate_verification_code(user, 'password_recovery')


class RecoverySetPasswordSerializer(serializers.Serializer):
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError("Passwords do not match.")
        return attrs

    def save(self, email):
        user = User.objects.get(email=email)
        user.set_password(self.validated_data['password'])
        user.is_active = True
        user.save()


