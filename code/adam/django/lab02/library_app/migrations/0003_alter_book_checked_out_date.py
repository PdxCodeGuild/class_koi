# Generated by Django 4.0.4 on 2022-04-29 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0002_book_checked_in_date_book_checked_out_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='checked_out_date',
            field=models.DateField(blank=True, null=True, verbose_name='date checked-out'),
        ),
    ]
