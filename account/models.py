from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    username = models.CharField(max_length=150, blank=True, null=True)
    email = models.EmailField('email address', unique=True)

    # Virtual Coin Accounts
    amd_balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    usd_balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    rub_balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    
    # Crypto Coin Accounts
    bitcoin_balance = models.DecimalField(max_digits=15, decimal_places=8, default=0.00000000)
    ethereum_balance = models.DecimalField(max_digits=15, decimal_places=8, default=0.00000000)
    xrp_balance = models.DecimalField(max_digits=15, decimal_places=8, default=0.00000000)
    tether_balance = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)
    bnb_balance = models.DecimalField(max_digits=15, decimal_places=8, default=0.00000000)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name'] 

    

