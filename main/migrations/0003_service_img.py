# Generated by Django 4.2.15 on 2024-08-13 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_banners'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='img',
            field=models.ImageField(null=True, upload_to='services/'),
        ),
    ]
