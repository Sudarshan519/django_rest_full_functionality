# Generated by Django 4.1.7 on 2023-04-02 15:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0020_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='currencyrate',
            name='created_at',
            field=models.DateField(default=datetime.datetime.now, verbose_name='Created Date'),
        ),
        migrations.AddField(
            model_name='currencyrate',
            name='update_at',
            field=models.DateField(default=datetime.datetime.now, verbose_name='Updated Date'),
        ),
        migrations.AlterField(
            model_name='country',
            name='estimate',
            field=models.CharField(max_length=50, verbose_name='Estimate'),
        ),
        migrations.AlterField(
            model_name='country',
            name='estimate2',
            field=models.CharField(max_length=50, verbose_name='Estimate2'),
        ),
        migrations.AlterField(
            model_name='country',
            name='year',
            field=models.CharField(max_length=50, verbose_name='Year'),
        ),
        migrations.AlterField(
            model_name='currencyrate',
            name='sell',
            field=models.FloatField(verbose_name='Sell'),
        ),
        migrations.AlterField(
            model_name='currencyrate',
            name='unit',
            field=models.IntegerField(default=1, verbose_name='Unit'),
        ),
    ]
