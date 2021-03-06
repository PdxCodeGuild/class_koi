# Generated by Django 4.0.4 on 2022-05-03 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0005_rename_book_title_checkout_book_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checkout',
            name='checked_in_date',
        ),
        migrations.RemoveField(
            model_name='checkout',
            name='checked_out_date',
        ),
        migrations.AddField(
            model_name='book',
            name='checked_in_date',
            field=models.DateField(blank=True, null=True, verbose_name='date checked in'),
        ),
        migrations.AddField(
            model_name='book',
            name='checked_out_date',
            field=models.DateField(blank=True, null=True, verbose_name='date checked-out'),
        ),
    ]
