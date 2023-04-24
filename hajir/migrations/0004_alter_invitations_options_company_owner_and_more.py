# Generated by Django 4.1.7 on 2023-04-22 07:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hajir', '0003_employee_employee_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='invitations',
            options={'ordering': ('-company',)},
        ),
        migrations.AddField(
            model_name='company',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='invitations',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hajir.employee', verbose_name='Employe'),
        ),
    ]