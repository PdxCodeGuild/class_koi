# Generated by Django 4.0.4 on 2022-04-29 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_book_date_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='date_published',
            field=models.DateField(blank=True, null=True, verbose_name='date published'),
        ),
    ]
