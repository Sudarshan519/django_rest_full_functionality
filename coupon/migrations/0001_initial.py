# Generated by Django 4.1.5 on 2023-09-05 06:10

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50, unique=True)),
                ('discount_percentage', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('disacount_amount', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('valid_from', models.DateField()),
                ('valid_to', models.DateField()),
                ('max_usage_count', models.PositiveIntegerField()),
                ('current_usage_count', models.PositiveIntegerField(default=0)),
                ('users_redeemed', models.ManyToManyField(blank=True, related_name='redeemed_coupons', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
