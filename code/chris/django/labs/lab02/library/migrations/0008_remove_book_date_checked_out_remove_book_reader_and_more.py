# Generated by Django 4.0.4 on 2022-04-29 23:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0007_book_date_checked_out'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='date_checked_out',
        ),
        migrations.RemoveField(
            model_name='book',
            name='reader',
        ),
        migrations.CreateModel(
            name='CheckOut',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reader', models.CharField(blank=True, max_length=100, null=True)),
                ('date_checked_out', models.DateField(verbose_name='date checked out')),
                ('date_returned', models.DateField(verbose_name='date returned')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='checkouts', to='library.book')),
            ],
        ),
    ]