# Generated by Django 4.0.4 on 2022-05-09 18:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chirp', '0003_chirppost_user_alter_chirppost_date_posted'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chirppost',
            name='author',
        ),
    ]
