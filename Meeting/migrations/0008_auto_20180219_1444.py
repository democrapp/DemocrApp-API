# Generated by Django 2.0.2 on 2018-02-19 14:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Meeting', '0007_auto_20180219_1429'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='authtoken',
            name='created_at',
        ),
        migrations.AddField(
            model_name='tokenset',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]