# Generated by Django 4.0.4 on 2022-05-02 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game_of_thrones', '0003_character_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='img_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
