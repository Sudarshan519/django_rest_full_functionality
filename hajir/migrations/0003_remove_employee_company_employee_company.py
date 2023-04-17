# Generated by Django 4.1.7 on 2023-04-15 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hajir', '0002_employee_employee_id_alter_employee_customuser_ptr'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='company',
        ),
        migrations.AddField(
            model_name='employee',
            name='company',
            field=models.ManyToManyField(to='hajir.company', verbose_name='Company List'),
        ),
    ]
