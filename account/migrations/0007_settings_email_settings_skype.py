# Generated by Django 5.1.3 on 2024-12-08 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_customuser_address_customuser_city_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='settings',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='settings',
            name='skype',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
