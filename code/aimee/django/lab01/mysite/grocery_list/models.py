from django.db import models

class GroceryItem(models.Model):
    description = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date created', auto_now_add=True)
    done_date = models.DateTimeField('date completed', null=True, blank=True)
    check_completed = models.BooleanField(default=False)
    def __str__(self):
        return self.description 

# Cannot resolve keyword 'completed' into field. Choices are: check_completed, description, done_date, id, pub_date
# when trying to go to home page /grocery_list
class Meta:
    verbose_name_plural = 'Groceries'
