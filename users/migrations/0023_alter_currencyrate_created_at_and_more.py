# Generated by Django 4.1.7 on 2023-04-02 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0022_alter_currencyrate_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currencyrate',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created Date'),
        ),
        migrations.AlterField(
            model_name='currencyrate',
            name='update_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated Date'),
        ),
    ]
