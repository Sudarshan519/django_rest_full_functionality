# Generated by Django 4.1.5 on 2023-03-21 09:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0018_profiledocuments_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profiledocuments',
            options={'ordering': ('-created_at',)},
        ),
    ]
