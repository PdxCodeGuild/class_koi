# Generated by Django 4.0.4 on 2022-04-27 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grocery_list', '0002_alter_groceryitem_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groceryitem',
            name='done_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='date completed'),
        ),
    ]