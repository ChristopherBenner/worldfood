from django.db import models
from recipes.models import Recipe
from django.contrib.auth.models import User
# Create your models here.
class Comment(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete = models.CASCADE, related_name = 'comments')
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add = True)
    parent = models.ForeignKey('self', null=True, blank=True, related_name = 'replies', on_delete = models.CASCADE)

    def __str__(self):
        return f"{self.recipe.name} | {self.author} | {self.text[:50]}"
