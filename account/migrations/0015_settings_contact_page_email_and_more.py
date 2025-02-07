# Generated by Django 5.1.3 on 2025-01-20 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0014_alter_customuser_is_approved'),
    ]

    operations = [
        migrations.AddField(
            model_name='settings',
            name='contact_page_email',
            field=models.EmailField(blank=True, max_length=254, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='settings',
            name='contact_page_skype',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
