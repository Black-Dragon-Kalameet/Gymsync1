# Generated by Django 4.2.15 on 2024-08-31 09:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_notifuserstatus'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notifuserstatus',
            old_name='notif',
            new_name='notification',
        ),
    ]
