# Generated by Django 4.0.4 on 2022-05-02 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_alter_book_pub_date_alter_checkout_checkout'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkout',
            name='checkout',
            field=models.BooleanField(default=False),
        ),
    ]
