# Generated by Django 4.1.7 on 2023-03-10 19:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_profile_country_of_residence_profile_passport_number_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='password_image',
        ),
        migrations.AlterField(
            model_name='profile',
            name='passport_number',
            field=models.CharField(default='1234', max_length=50, verbose_name='Passport Number'),
        ),
        migrations.CreateModel(
            name='UserDocuments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password_image', models.FileField(blank=True, null=True, upload_to=None, verbose_name='Passport Images')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='documents',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.userdocuments', verbose_name=''),
        ),
    ]
