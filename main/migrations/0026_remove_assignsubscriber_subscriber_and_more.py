# Generated by Django 4.2.15 on 2024-09-06 18:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0025_rename_notification_notifuserstatus_notif_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assignsubscriber',
            name='subscriber',
        ),
        migrations.AddField(
            model_name='assignsubscriber',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
