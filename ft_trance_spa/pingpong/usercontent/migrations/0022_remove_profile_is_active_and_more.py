# Generated by Django 5.0.4 on 2024-10-31 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usercontent', '0021_alter_profile_tournament_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='is_active',
        ),
        migrations.AlterField(
            model_name='profile',
            name='tournament_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]