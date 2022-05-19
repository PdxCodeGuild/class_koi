from django.db import models

class NutritionFacts(models.Model):
    name = models.CharField(max_length=50)
    serving_size = models.IntegerField('Serving Size (g)')
    calories = models.IntegerField()
    fat = models.IntegerField('Fat (g)')
    carbs = models.IntegerField('Carbohydrates (g)')
    protein = models.IntegerField('Protein (g)')
    image = models.ImageField(null=True)

    class Meta:
        verbose_name_plural = 'Nutrition Facts'

    def __str__(self):
        return f'{self.name} ({self.serving_size}g)'