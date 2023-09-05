# Generated by Django 4.1.5 on 2023-09-05 06:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_transactions_coupon_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecipientTransactionType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_type', models.IntegerField(choices=[(0, 'Credit Card'), (2, 'Bank'), (3, 'Cash'), (4, 'Wallet')], verbose_name='Transactions type')),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('account_number', models.IntegerField(verbose_name='Account Number')),
            ],
        ),
        migrations.AddField(
            model_name='transactions',
            name='recipient',
            field=models.CharField(default=1, max_length=150, verbose_name='Recipient'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='transactions',
            name='recipient_transaction_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='users.recipienttransactiontype'),
            preserve_default=False,
        ),
    ]