# Generated by Django 4.0.4 on 2022-05-02 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0006_alter_checkout_checkout'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='slug',
            field=models.SlugField(default='book'),
            preserve_default=False,
        ),
    ]