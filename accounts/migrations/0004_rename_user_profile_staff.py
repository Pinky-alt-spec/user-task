# Generated by Django 3.2.8 on 2021-10-14 11:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_profile_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='user',
            new_name='staff',
        ),
    ]
