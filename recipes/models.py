from django.db import models
from django.template.defaultfilters import slugify

from countries.models import Country
class Recipe(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(default='')
    ingredients = models.TextField(null=True, blank=True)
    instructions = models.TextField(null=True, blank=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    # Things to add later: pictures, ratings, comments

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
