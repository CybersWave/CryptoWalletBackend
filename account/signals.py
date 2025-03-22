from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import (
    CustomUser,
    CryptoCurrency,
    VirtualCurrency,
    CryptoWallet,
    VirtualWallet,
    CryptoWalletItem,
    VirtualWalletItem
)


@receiver(post_save, sender=CustomUser)
def create_user_wallets(sender, instance, created, **kwargs):
    if created:
        CryptoWallet.objects.create(user=instance)
        VirtualWallet.objects.create(user=instance)


@receiver(post_save, sender=CryptoCurrency)
def add_new_crypto_to_all_wallets(sender, instance, created, **kwargs):
    if created:
        for wallet in CryptoWallet.objects.all():
            if not CryptoWalletItem.objects.filter(wallet=wallet, currency=instance).exists():
                CryptoWalletItem.objects.create(wallet=wallet, currency=instance, amount=0.0)


@receiver(post_save, sender=VirtualCurrency)
def add_new_virtual_to_all_wallets(sender, instance, created, **kwargs):
    if created:
        for wallet in VirtualWallet.objects.all():
            if not VirtualWalletItem.objects.filter(wallet=wallet, currency=instance).exists():
                VirtualWalletItem.objects.create(wallet=wallet, currency=instance, amount=0.0)
