# Generated by Django 4.0.4 on 2022-05-09 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_remove_user_checkout_book_checked_out_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='checked_out',
        ),
        migrations.AddField(
            model_name='user',
            name='checkout',
            field=models.BooleanField(default=False),
        ),
    ]
