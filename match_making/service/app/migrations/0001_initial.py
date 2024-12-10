# Generated by Django 3.1 on 2024-11-12 14:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='queue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('socket_id', models.CharField(max_length=255, unique=True, verbose_name='socket')),
                ('joined_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='create date')),
                ('login', models.CharField(max_length=50, null=True, verbose_name='login')),
                ('groupe', models.CharField(max_length=50, null=True, verbose_name='groupe')),
            ],
        ),
    ]