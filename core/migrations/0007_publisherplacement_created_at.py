# Generated by Django 5.1.3 on 2024-11-29 09:41

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_publisherplacement_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='publisherplacement',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
