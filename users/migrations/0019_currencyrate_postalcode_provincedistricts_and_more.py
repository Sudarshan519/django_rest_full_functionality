# Generated by Django 4.1.7 on 2023-03-26 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0018_profiledocuments_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='CurrencyRate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iso3', models.CharField(max_length=50, verbose_name='ISO3')),
                ('name', models.CharField(max_length=50, verbose_name='NAME')),
                ('unit', models.IntegerField(verbose_name='Unit')),
                ('buy', models.FloatField(verbose_name='Buy')),
                ('sell', models.DurationField(verbose_name='Sell')),
            ],
        ),
        migrations.CreateModel(
            name='PostalCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(default='Nepal', max_length=100)),
                ('district', models.CharField(default='', max_length=255)),
                ('post_office', models.CharField(max_length=50, verbose_name='Post office')),
                ('postal_pin_code', models.CharField(max_length=100, verbose_name='Postal/Pin Code')),
                ('postal_office_type', models.CharField(max_length=50, verbose_name='Post Office Type')),
            ],
        ),
        migrations.CreateModel(
            name='ProvinceDistricts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(default='Nepal', max_length=100)),
                ('district', models.CharField(default='', max_length=255)),
                ('province', models.CharField(default='', max_length=255)),
            ],
        ),
        migrations.AlterModelOptions(
            name='profiledocuments',
            options={'ordering': ('-created_at',)},
        ),
    ]
