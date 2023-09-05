from django.db import models

from users.models import CustomUser

# Create your models here.
class JapanBankAccount(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    account_name=models.CharField(max_length=60, unique=True,default='',blank=True)
    account_number = models.CharField(max_length=20, unique=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    opened_date = models.DateField(auto_now_add=True)

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.save()

    def withdraw(self, amount):
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            self.save()

    def __str__(self):
        return f"Account: {self.account_number}, Balance: ${self.balance}"