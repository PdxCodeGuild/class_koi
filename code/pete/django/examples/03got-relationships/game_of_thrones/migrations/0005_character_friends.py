# Generated by Django 4.0.4 on 2022-05-02 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game_of_thrones', '0004_character_img_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='friends',
            field=models.ManyToManyField(to='game_of_thrones.character'),
        ),
    ]
