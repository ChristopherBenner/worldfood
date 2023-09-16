from django.db import models
from django.contrib.auth.models import User
from recipes.models import Recipe

class Dashboard(models.Model):
    user = models.ForeignKey(User, related_name='dashboard', on_delete=models.CASCADE)
    saved_recipes = models.ManyToManyField(Recipe, related_name='saved_recipes')
    made_recipes = models.ManyToManyField(Recipe, related_name='made_recipes')

    def __str__(self):
        return self.user.username + "'s Dashboard"
