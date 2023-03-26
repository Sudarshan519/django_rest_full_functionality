# Generated by Django 4.1.7 on 2023-03-10 19:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile_residencetype_customuser_resident_type_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='country_of_residence',
            field=models.CharField(default='Japan', max_length=50, verbose_name='Country of residence'),
        ),
        migrations.AddField(
            model_name='profile',
            name='passport_number',
            field=models.CharField(default='1234', max_length=50, verbose_name='Password Number'),
        ),
        migrations.AddField(
            model_name='profile',
            name='password_image',
            field=models.FileField(blank=True, null=True, upload_to=None, verbose_name='Password Images'),
        ),
        migrations.AddField(
            model_name='profile',
            name='profession',
            field=models.CharField(default='', max_length=50, verbose_name='Profession'),
        ),
        migrations.AddField(
            model_name='profile',
            name='profile_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='users.residencetype'),
        ),
        migrations.AddField(
            model_name='profile',
            name='status_of_residence',
            field=models.CharField(default='Skilled Professional', max_length=100, verbose_name='Status of residence'),
        ),
        migrations.AddField(
            model_name='profile',
            name='title',
            field=models.IntegerField(choices=[(1, 'Mr'), (2, 'Mrs')], default=1),
        ),
    ]
