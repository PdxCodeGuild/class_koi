# Generated by Django 4.0.4 on 2022-05-27 17:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='titles',
            new_name='title',
        ),
    ]
