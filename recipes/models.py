from django.db import models
from django.template.defaultfilters import slugify

from countries.models import Country
class Recipe(models.Model):
    name = models.CharField(max_length=255)
    ingredients = models.TextField(null=True, blank=True)
    instructions = models.TextField(null=True, blank=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    # Things to add later: pictures, ratings, comments

    def slug(self):
        return slugify(self.name)
