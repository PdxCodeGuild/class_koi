# Generated by Django 4.0.4 on 2022-05-06 21:12

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_alter_chirp_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chirp',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 6, 21, 12, 3, 31479, tzinfo=utc)),
        ),
    ]