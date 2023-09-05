from django.db import models

from users.models import CustomUser

# Create your models here.
class Coupon(models.Model):
    code = models.CharField(max_length=50, unique=True)
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2,null=True)
    disacount_amount=models.DecimalField(max_digits=5, decimal_places=2,null=True)
    valid_from = models.DateField()
    valid_to = models.DateField()
    max_usage_count = models.PositiveIntegerField()
    current_usage_count = models.PositiveIntegerField(default=0)
    users_redeemed = models.ManyToManyField(CustomUser, blank=True, related_name='redeemed_coupons')
    def is_valid(self):
        from django.utils import timezone
        today = timezone.now().date()
        return self.valid_from <= today <= self.valid_to and self.current_usage_count < self.max_usage_count

    def apply_discount(self, original_price):
        return original_price - (original_price * (self.discount_percentage / 100))