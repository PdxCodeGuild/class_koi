# Generated by Django 4.0.4 on 2022-05-06 20:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_rename_user_posts_author_remove_posts_title_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='date_written',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='date chirped'),
        ),
    ]
