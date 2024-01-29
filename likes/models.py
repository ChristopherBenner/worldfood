from django.db import models
from recipes.models import Recipe
from django.contrib.auth.models import User

class Like(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    liked_on = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"{self.recipe} | {self.user.username} | {self.liked_on}"