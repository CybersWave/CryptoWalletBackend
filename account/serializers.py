from rest_framework import serializers
from .models import (
    CustomUser,
    CryptoCurrency,
    VirtualCurrency,
    CryptoWallet,
    VirtualWallet,
    CryptoWalletItem,
    VirtualWalletItem
)


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
        model = CustomUser
        fields = [
            'userID', 'email', 'first_name', 'last_name', 'img',
            'phone_number', 'dob', 'country',
            'crypto_wallet', 'virtual_wallet'
        ]
