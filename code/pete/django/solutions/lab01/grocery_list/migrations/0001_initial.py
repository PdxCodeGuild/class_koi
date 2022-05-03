# Generated by Django 4.0.4 on 2022-05-03 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GroceryItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=50)),
                ('created_date', models.DateField()),
                ('completed_date', models.DateField()),
                ('completed', models.BooleanField()),
            ],
        ),
    ]
