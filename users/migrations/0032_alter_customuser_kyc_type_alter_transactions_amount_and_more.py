# Generated by Django 4.1.7 on 2023-04-08 15:26

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0031_customuser_kyc_type_alter_transactions_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='kyc_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='users.ekyctype'),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='amount',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(10.0)], verbose_name='Transaction Amount'),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='charge_amount',
            field=models.FloatField(default=50.0, verbose_name='Charge Amount'),
        ),
    ]