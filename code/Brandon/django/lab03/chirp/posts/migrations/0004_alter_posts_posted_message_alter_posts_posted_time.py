# Generated by Django 4.0.4 on 2022-05-15 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_rename_post_posts_posted_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='posted_message',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='posts',
            name='posted_time',
            field=models.CharField(blank=True, default='hi', max_length=40),
            preserve_default=False,
        ),
    ]
