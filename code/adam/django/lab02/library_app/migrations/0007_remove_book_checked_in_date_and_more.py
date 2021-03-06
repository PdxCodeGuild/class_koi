# Generated by Django 4.0.4 on 2022-05-03 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0006_remove_checkout_checked_in_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='checked_in_date',
        ),
        migrations.RemoveField(
            model_name='book',
            name='checked_out_date',
        ),
        migrations.AddField(
            model_name='checkout',
            name='checked_in_date',
            field=models.DateField(blank=True, null=True, verbose_name='date checked in'),
        ),
        migrations.AddField(
            model_name='checkout',
            name='checked_out_date',
            field=models.DateField(blank=True, null=True, verbose_name='date checked-out'),
        ),
    ]
