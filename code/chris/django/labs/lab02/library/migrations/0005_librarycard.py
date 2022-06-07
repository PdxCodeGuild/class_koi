# Generated by Django 4.0.4 on 2022-04-29 21:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0004_alter_book_date_published'),
    ]

    operations = [
        migrations.CreateModel(
            name='LibraryCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reader', models.CharField(max_length=100)),
                ('date_checked_out', models.DateField(blank=True, null=True, verbose_name='date checked out')),
                ('date_returned', models.DateField(blank=True, null=True, verbose_name='date returned')),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='record', to='library.book')),
            ],
        ),
    ]