# Generated by Django 3.0.8 on 2022-12-15 06:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('multiaudio', '0002_auto_20221215_1140'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stream',
            name='room_slug',
        ),
        migrations.AddField(
            model_name='stream',
            name='slug',
            field=models.CharField(blank=True, max_length=244),
        ),
        migrations.AlterField(
            model_name='stream',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 15, 11, 41, 56, 316955)),
        ),
    ]