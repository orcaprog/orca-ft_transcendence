# Generated by Django 3.1 on 2024-11-15 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='queue',
            name='player_id',
            field=models.IntegerField(default=-1, unique=True, verbose_name='player_id'),
        ),
    ]