# Generated by Django 4.0.4 on 2022-04-28 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grocery_list', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='groceryitem',
            name='completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='groceryitem',
            name='completed_date',
            field=models.DateTimeField(default=False),
        ),
        migrations.AlterField(
            model_name='groceryitem',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
