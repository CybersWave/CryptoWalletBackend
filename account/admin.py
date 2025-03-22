from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import (
    CustomUser,
    CryptoCurrency,
    VirtualCurrency,
    CryptoWallet,
    VirtualWallet,
    CryptoWalletItem,
    VirtualWalletItem
)


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser

    list_display = ('email', 'userID', 'first_name', 'last_name', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'country')
    search_fields = ('email', 'first_name', 'last_name', 'userID')
    ordering = ('email',)
    readonly_fields = ('userID',)


    fieldsets = (
        (None, {
            'fields': ('email', 'password')
        }),
        ('Personal Info', {
            'fields': (
                'userID', 'first_name', 'last_name', 'img',
                'phone_number', 'dob', 'country'
            )
        }),
        ('Permissions', {
            'fields': (
                'is_active', 'is_staff', 'is_superuser',
                'groups', 'user_permissions'
            )
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        }),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email', 'password1', 'password2',
                'userID', 'first_name', 'last_name', 'img',
                'phone_number', 'dob', 'country'
            )
        }),
    )

    filter_horizontal = ('groups', 'user_permissions',)


@admin.register(CryptoCurrency)
class CryptoCurrencyAdmin(admin.ModelAdmin):
    list_display = ('name', 'icon')
    search_fields = ('name',)


@admin.register(VirtualCurrency)
class VirtualCurrencyAdmin(admin.ModelAdmin):
    list_display = ('name', 'icon')
    search_fields = ('name',)


@admin.register(CryptoWallet)
class CryptoWalletAdmin(admin.ModelAdmin):
    list_display = ('user',)
    search_fields = ('user__email', 'user__userID')


@admin.register(VirtualWallet)
class VirtualWalletAdmin(admin.ModelAdmin):
    list_display = ('user',)
    search_fields = ('user__email', 'user__userID')


@admin.register(CryptoWalletItem)
class CryptoWalletItemAdmin(admin.ModelAdmin):
    list_display = ('wallet', 'currency', 'amount')
    list_filter = ('currency',)
    search_fields = ('wallet__user__email', 'currency__name')


@admin.register(VirtualWalletItem)
class VirtualWalletItemAdmin(admin.ModelAdmin):
    list_display = ('wallet', 'currency', 'amount')
    list_filter = ('currency',)
    search_fields = ('wallet__user__email', 'currency__name')
