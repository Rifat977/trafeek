# Generated by Django 5.1.3 on 2025-01-27 12:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0025_subid_icon'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subid',
            name='icon',
        ),
    ]
