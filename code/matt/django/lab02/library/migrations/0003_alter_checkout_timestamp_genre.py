# Generated by Django 4.0.4 on 2022-04-27 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_checkout'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkout',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.CharField(max_length=50)),
                ('books', models.ManyToManyField(to='library.book')),
            ],
        ),
    ]
