# Generated by Django 4.0.4 on 2022-04-27 22:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grocery_list_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groceryitem',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='date added'),
        ),
    ]
