# Generated by Django 4.1.7 on 2023-03-11 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_customuser_counter'),
    ]

    operations = [
        migrations.CreateModel(
            name='TermsAndConditions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Type')),
                ('detail', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='customuser',
            name='is_business_user',
            field=models.BooleanField(default=False),
        ),
    ]
