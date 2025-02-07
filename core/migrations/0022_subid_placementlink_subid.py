# Generated by Django 5.1.3 on 2024-12-19 21:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_alter_notice_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubID',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('slug', models.CharField(blank=True, max_length=255, null=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='Active')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
            ],
            options={
                'verbose_name': 'SubID',
                'verbose_name_plural': 'SubIDs',
                'ordering': ['-created_at'],
            },
        ),
        migrations.AddField(
            model_name='placementlink',
            name='subid',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.subid'),
            preserve_default=False,
        ),
    ]
