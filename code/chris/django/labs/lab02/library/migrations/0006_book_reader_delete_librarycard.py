# Generated by Django 4.0.4 on 2022-04-29 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0005_librarycard'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='reader',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.DeleteModel(
            name='LibraryCard',
        ),
    ]
