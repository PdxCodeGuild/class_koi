# Generated by Django 4.0.4 on 2022-06-28 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0005_checkout_delete_member'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkout',
            name='checkout',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
