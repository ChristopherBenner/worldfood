from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

from countries.models import Country
class Recipe(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(default='')
    ingredients = models.TextField(null=True, blank=True)
    instructions = models.TextField(null=True, blank=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    # saved_recipes = models.ManyToManyField(User, related_name='saved_recipe')
    # made_recipes = models.ManyToManyField(User, related_name='made_recipe')
    # Things to add later: pictures, ratings, comments

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class SavedRecipe(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Saved Recipes"

    def __str__(self):
        return f"{self.user.username} | {self.recipe.name}"
    
    

class MadeRecipe(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Made Recipes"

    def __str__(self):
        return f"{self.user.username} | {self.recipe.name}"