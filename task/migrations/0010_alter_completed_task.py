# Generated by Django 3.2.8 on 2021-10-13 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0009_auto_20211013_2202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='completed',
            name='task',
            field=models.CharField(max_length=200, null=True),
        ),
    ]