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
    saved_recipes = models.ManyToManyField(User, related_name='saved_recipe')
    # Things to add later: pictures, ratings, comments

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
