# Generated by Django 3.2.8 on 2021-10-13 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_remove_profile_firstname'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='man.jpeg', upload_to='images'),
        ),
    ]
