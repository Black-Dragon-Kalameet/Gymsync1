# Generated by Django 4.2.15 on 2024-09-07 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0037_traineracheivement'),
    ]

    operations = [
        migrations.AddField(
            model_name='traineracheivement',
            name='date',
            field=models.DateField(null=True),
        ),
    ]
