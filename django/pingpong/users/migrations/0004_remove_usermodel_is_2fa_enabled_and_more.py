# Generated by Django 5.1 on 2024-09-02 09:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_usermodel_is_2fa_enabled_usermodel_two_factor_secret'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usermodel',
            name='is_2fa_enabled',
        ),
        migrations.RemoveField(
            model_name='usermodel',
            name='two_factor_secret',
        ),
    ]
