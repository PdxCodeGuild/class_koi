# Generated by Django 4.0.4 on 2022-05-03 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0008_alter_checkout_book_genre'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='genre',
            name='books',
        ),
        migrations.AddField(
            model_name='book',
            name='genres',
            field=models.ManyToManyField(related_name='books', to='library_app.genre'),
        ),
    ]