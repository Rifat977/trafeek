# Generated by Django 5.1.3 on 2025-01-21 19:32

import django.contrib.auth.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0015_settings_contact_page_email_and_more'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomGroup',
            fields=[
            ],
            options={
                'verbose_name': 'Permissions',
                'verbose_name_plural': 'Permissions',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('auth.group',),
            managers=[
                ('objects', django.contrib.auth.models.GroupManager()),
            ],
        ),
    ]
