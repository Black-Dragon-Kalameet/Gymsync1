# Generated by Django 4.2.15 on 2024-09-07 08:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0030_subscription_reg_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='banners',
            options={'verbose_name_plural': 'Banners'},
        ),
        migrations.AlterModelOptions(
            name='enquiry',
            options={'verbose_name_plural': 'Enquiries'},
        ),
        migrations.AlterModelOptions(
            name='gallery',
            options={'verbose_name_plural': 'Galleries'},
        ),
        migrations.AlterModelOptions(
            name='notify',
            options={'verbose_name_plural': 'Notifications'},
        ),
    ]
