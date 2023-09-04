from django.db import models

from products.models import Product
from users.models import CustomUser



class Payment(models.Model):
    payment_for_order = models.ForeignKey('Order', on_delete=models.CASCADE,related_name="payment_for_order")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)
    # Add more fields as needed, e.g., payment status, payment method, etc.
# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    #  Add a field to link the order to its payment
    payment = models.ForeignKey('Payment', null=True, blank=True, on_delete=models.SET_NULL)