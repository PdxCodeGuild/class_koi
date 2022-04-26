from django.db import models

class GroceryItem(models.Model):
    description = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date created')
    done_date = models.DateTimeField('date completed')
    check_completed = models.BooleanField()
    def __str__(self):
        return self.description 

# Cannot resolve keyword 'completed' into field. Choices are: check_completed, description, done_date, id, pub_date
# when trying to go to home page /grocery_list

