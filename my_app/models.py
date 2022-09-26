from django.db import models
from django.contrib.auth.hashers import make_password


# Create your models here.
class Bank(models.Model):
    name = models.CharField(max_length=100)


class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=False)
    phone_number = models.CharField(max_length=100)
    bank = models.ForeignKey(Bank,on_delete=models.CASCADE,related_name="users")

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Account(models.Model):
    account_name = models.CharField(max_length=100, null=False)
    account_number = models.CharField(max_length=100, null=False)
    account_balance = models.DecimalField(max_digits=100, decimal_places=2)
    account_password = models.CharField(max_length=20)
    user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)


class Transaction(models.Model):
    TRANSACTION_TYPE = (
        ("CREDIT", 'credit'),
        ("DEBIT", "debit")
    )

    narration = models.TextField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type = models.CharField(max_length=100, choices=TRANSACTION_TYPE)
    transaction_date = models.DateField(auto_now_add=True)
    balance_after_transaction = models.DecimalField(max_digits=10, decimal_places=2)
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="transactions")
