# Generated by Django 4.0.4 on 2022-05-06 17:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grocery_list', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={'ordering': ['complete', '-date_created']},
        ),
    ]