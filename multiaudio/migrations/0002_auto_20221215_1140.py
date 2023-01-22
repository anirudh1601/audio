# Generated by Django 3.0.8 on 2022-12-15 06:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('multiaudio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='stream',
            name='room_slug',
            field=models.SlugField(blank=True, unique=True),
        ),
        migrations.AlterField(
            model_name='stream',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 15, 11, 40, 10, 120080)),
        ),
    ]