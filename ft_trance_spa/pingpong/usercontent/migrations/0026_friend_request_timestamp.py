# Generated by Django 5.0.4 on 2024-11-16 16:12

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usercontent', '0025_alter_friend_request_receiver_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='friend_request',
            name='timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
