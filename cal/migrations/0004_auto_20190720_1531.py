# Generated by Django 2.2.3 on 2019-07-20 06:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cal', '0003_auto_20190720_1531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='end_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 7, 20, 15, 31, 37, 83385)),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 7, 20, 15, 31, 37, 82382)),
        ),
    ]