# Generated by Django 4.2.15 on 2024-09-07 09:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0032_alter_faq_options_trainer_facebook_trainer_pinterest_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='trainer',
            old_name='x',
            new_name='twitter',
        ),
    ]
