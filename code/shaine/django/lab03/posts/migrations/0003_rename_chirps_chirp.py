# Generated by Django 4.0.4 on 2022-05-13 18:47

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0002_rename_chirp_chirps'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Chirps',
            new_name='Chirp',
        ),
    ]
