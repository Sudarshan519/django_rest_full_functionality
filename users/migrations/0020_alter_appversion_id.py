# Generated by Django 4.1.5 on 2023-03-21 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0019_alter_profiledocuments_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appversion',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
