# Generated by Django 4.0.4 on 2022-04-27 17:28

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('grocerylist', '0002_alter_grocery_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grocery',
            name='completed_date',
            field=models.DateField(default=None, null=None),
        ),
        migrations.AlterField(
            model_name='grocery',
            name='created_date',
            field=models.DateField(default=datetime.datetime(2022, 4, 27, 17, 28, 16, 222493, tzinfo=utc)),
        ),
    ]
