# Generated by Django 4.1.7 on 2023-03-13 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_rename_isverified_customuser_emailverified_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='gps',
            field=models.CharField(default='', max_length=60),
        ),
        migrations.AddField(
            model_name='ekyc',
            name='created_at',
            field=models.DateTimeField(auto_now=True, verbose_name=''),
        ),
    ]