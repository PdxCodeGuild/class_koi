# Generated by Django 4.0.4 on 2022-05-05 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NutritionFacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('calories', models.IntegerField()),
                ('fat', models.IntegerField(verbose_name='Fat (g)')),
                ('carbs', models.IntegerField(verbose_name='Carbohydrates (g)')),
                ('protein', models.IntegerField(verbose_name='Protein (g)')),
                ('serving_size', models.IntegerField(verbose_name='Serving Size (g)')),
            ],
        ),
    ]
