# Generated by Django 3.2.8 on 2021-10-13 16:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='current',
            old_name='name',
            new_name='tasks',
        ),
        migrations.AlterField(
            model_name='current',
            name='date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.CreateModel(
            name='Completed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveBigIntegerField(null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('task', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='task.current')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
