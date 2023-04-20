# Generated by Django 4.1.7 on 2023-04-02 16:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0026_remove_currencyrate_created_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='currencyrate',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Created Date'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='currencyrate',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated Date'),
        ),
    ]
