# Generated by Django 4.0.4 on 2022-04-26 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('population', models.IntegerField()),
                ('climate', models.CharField(choices=[('TR', 'Tropical'), ('DR', 'Dry'), ('TE', 'Temperate'), ('CT', 'Continental'), ('PO', 'Polar')], max_length=2)),
                ('visited', models.BooleanField(default=False)),
            ],
        ),
    ]